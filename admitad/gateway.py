from django.conf import settings
import requests


def send_order_creation_request(order, currency_code='rub', payment_type='sale'):
    admitad_currency_code = currency_code
    admitad_action_code = None  # TODO: ???
    admitad_tariff_code = None  # TODO: ???
    admitad_postback = 1  # TODO: ???
    admitad_payment_type = payment_type
    admitad_uuid = settings.ADMITAD_UUID
    admitad_postback_url = settings.ADMITAD_POSTBACK_URL

    admitad_campaign_code = settings.ADMITAD_COMPAIN_CODE

    base_args = {
        'uid': admitad_uuid,
        'campaign_code': admitad_campaign_code,
        'order_id': order.internal_id,
        'action_code': admitad_action_code,
        'tariff_code': admitad_tariff_code,
        'currency_code': admitad_currency_code,
        'position_count': order.items_count,
        'payment_type': admitad_payment_type,
        'postback': admitad_postback,
        'postback_key': order.postback_key
    }

    for num, item in enumerate(order.items):
        request_args = base_args.copy()
        request_args.update({
            'position_id': num,
            'product_id': item.internal_id,
            'quantity': item.quantity,
            'price': item.item_price,
            'currency_code': item.currency_code
        })

        response = requests.get(admitad_postback_url, params=request_args)


class Order:
    """
    Order object
    """
    items = []

    def __init__(self, internal_id, postback_key, items=None):
        self.internal_id = internal_id
        self.postback_key = postback_key
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
