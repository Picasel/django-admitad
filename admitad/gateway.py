import requests
from django.conf import settings

from admitad.utils import add_params_to_url
from .models import AdmitadPostbackEvent, AdmitadPostbackRequest


class Order:
    """
    Order object
    """
    items = []

    def __init__(self, internal_id , admitad_uid, action_code, tariff_code,
                 payment_type=AdmitadPostbackEvent.SALE, items=None):

        self.internal_id = internal_id
        self.admitad_uid = admitad_uid
        self.action_code = action_code
        self.tariff_code = tariff_code
        self.payment_type = payment_type

        if items:
            self.items += items

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__

    def add_item(self, item):
        """
        Adds item t order
        """
        self.items.append(item)
        return True

    @property
    def full_price(self):
        """
        Returns order full price
        """
        price = 0
        for item in self.items:
            price += item.full_price

        return price

    @property
    def items_count(self):
        """
        Returns the items count in the order
        """
        return len(self.items)

    def send_postback_requests(self):
        """
        Sends postback requests to Admitad
        :return:
        """
        event = AdmitadPostbackEvent.objects.create(
            order_id=self.internal_id,
            admitad_uid=self.admitad_uid,
            campaign_code=settings.ADMITAD_COMPAIN_CODE,
            payment_type=self.payment_type,
            action_code=self.action_code,
            tariff_code=self.tariff_code
        )

        is_failed = False
        for params in self._generate_postback_payload():
            postback_request = AdmitadPostbackRequest.objects.create(
                event=event,
                product_id=params['product_id'],
                position_id=params['position'],
                quantity=params['quantity'],
                currency_code=params['currency_code'],
                price=params['price'],
                request_url=add_params_to_url(settings.ADMITAD_POSTBACK_URL, params)
            )
            try:
                response = requests.get(postback_request.request_url)
            except requests.exceptions.RequestException as error:
                is_failed = True
                postback_request.mark_as_failed(error)
            else:
                if response.status_code != 200:
                    is_failed = True
                    postback_request.mark_as_failed(response.content)

                postback_request.mark_as.success()

        if is_failed:
            event.mark_as_failed()
            return False

        else:
            event.mark_as_success()
            return True

    def _generate_postback_payload(self):
        """
        Generates payload for postback requests
        """
        base_params = {
            'uid': self.admitad_uid,
            'campaign_code': settings.ADMITAD_COMPAIN_CODE,
            'order_id': self.internal_id,
            'action_code': self.action_code,
            'tariff_code': self.tariff_code,
            'position_count': self.items_count,
            'payment_type': self.payment_type,
            'postback': 1,
            'postback_key': settings.ADMITAD_POSTBACK_KEY
        }

        for position, item in enumerate(self.items):
            request_params = base_params.copy()
            request_params.update({
                'position_id': position,
                'product_id': item.internal_id,
                'quantity': item.quantity,
                'price': item.item_price,
                'currency_code': item.currency_code
            })

            yield request_params


class Item:
    """
    Item object
    """

    def __init__(self, internal_id, item_price, quantity=1, currency_code='rub'):
        self.internal_id = internal_id
        self.currency_code = currency_code
        self.item_price = item_price
        self.quantity = quantity

    def __eq__(self, obj):
        return self.__dict__ == obj.__dict__

    @property
    def price(self):
        """
        Returns price per item
        """
        return self.item_price

    @property
    def full_price(self):
        """
        Returns full price including quantity
        """
        return self.item_price * self.quantity
