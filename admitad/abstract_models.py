from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractAdmitadPostbackEvent(models.Model):
    order_id = models.PositiveIntegerField(
        _('Order ID')
    )

    admitad_uid = models.CharField(
        _('Admitad UID'),
        max_length=64
    )
    campaign_code = models.CharField(
        _('Campain code'),
        max_length=64
    )

    SALE, LEAD = 'Sale', 'Lead'
    PAYMENT_TYPES_CHOICES = (
        (SALE, _('Sale')),
        (LEAD, _('Lead')),
    )

    payment_type = models.CharField(
        _('Payment type'),
        choices=PAYMENT_TYPES_CHOICES,
        max_length=4
    )

    action_code = models.CharField(
        _('Action code'),
        max_length=64
    )

    tariff_code = models.CharField(
        _('Tariff code'),
        max_length=16
    )

    CREATED, SUCCESS, FAILED = 'Created', 'Success', 'Failed'
    INTEGRATION_STATUS_CHOICES = (
        (CREATED, _('Created')),
        (SUCCESS, _('Success')),
        (FAILED, _('Failed')),
    )

    integration_status = models.CharField(
        _('Integration status'),
        choices=INTEGRATION_STATUS_CHOICES,
        default=CREATED,
        max_length=16
    )

    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        _('Updated at'),
        auto_now=True
    )

    class Meta:
        abstract = True
        verbose_name = _('Admitad postback event')
        verbose_name_plural = _('Admitad postback events')

    def __str__(self):
        return str(self.pk)

    def mark_as_failed(self):
        """
        Marks request as failed
        """
        self.integration_status = self.FAILED
        self.save()

        return True

    def mark_as_success(self):
        """
        Marks request as success
        """
        self.integration_status = self.SUCCESS
        self.save()

        return True

    def requests_count(self):
        return self.requests.count()


class AbstractAdmitadPostbackRequest(models.Model):
    event = models.ForeignKey(
        'admitad.AdmitadPostbackEvent',
        on_delete=models.CASCADE,
        related_name='requests',
        verbose_name=_('Event')
    )

    product_id = models.PositiveIntegerField(
        _('Product ID')
    )

    position_id = models.PositiveIntegerField(
        _('Position ID')
    )

    quantity = models.PositiveIntegerField(
        _('Quantity')
    )

    currency_code = models.CharField(
        _('Currency_code'),
        max_length=3
    )

    price = models.DecimalField(
        _('Price'),
        decimal_places=2,
        max_digits=12
    )

    request_url = models.URLField(
        _('Request URL')
    )

    CREATED, SUCCESS, FAILED = 'Created', 'Success', 'Failed'
    INTEGRATION_STATUS_CHOICES = (
        (CREATED, _('Created')),
        (SUCCESS, _('Success')),
        (FAILED, _('Failed')),
    )

    integration_status = models.CharField(
        _('Integration status'),
        choices=INTEGRATION_STATUS_CHOICES,
        default=CREATED,
        max_length=16
    )

    error_text = models.TextField(
        _('Error text'),
        blank=True, null=True
    )

    class Meta:
        abstract = True
        verbose_name = _('Admitad postback request')
        verbose_name_plural = _('Admitad postback requests')

    def mark_as_failed(self, error_text=None):
        """
        Marks request as failed
        """
        self.integration_status = self.FAILED
        self.error_text = error_text
        self.save()

        return True

    def mark_as_success(self):
        """
        Marks request as success
        """
        self.integration_status = self.SUCCESS
        self.save()

        return True
