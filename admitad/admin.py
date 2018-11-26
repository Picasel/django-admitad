from .models import AdmitadPostbackEvent, AdmitadPostbackRequest
from django.contrib import admin


class AdmitadPostbackRequestInline(admin.TabularInline):
    model = AdmitadPostbackRequest


@admin.register(AdmitadPostbackEvent)
class AdmitadPostbackEventAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'admitad_uid', 'campaign_code', 'payment_type', 'requests_count', 'integration_status',)
    list_filter = ('integration_status', 'campaign_code', 'payment_type', 'tariff_code', 'action_code')
    search_fields = ('order_id', 'requests__product_id', 'requests__request_url', 'requests__error_text')
    inlines = (AdmitadPostbackRequestInline,)
