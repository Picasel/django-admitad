from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from django.core.checks import Error, register
from django.conf import settings

from admitad import REQUIRED_SETTINGS, DOCS_URL


class AdmitadConfig(AppConfig):
    name = 'admitad'
    verbose_name = _('django admitad')


@register
def settings_check(app_configs, **kwargs):
    errors = []

    for number, required_field in enumerate(REQUIRED_SETTINGS, start=1):
        if not hasattr(settings, required_field):
            errors.append(
                Error(
                    msg='{} not found'.format(required_field),
                    hint='Please, read installation guide ({})'.format(DOCS_URL),
                    obj='django-admitad',
                    id='admitad.S{}'.format(number),
                )
            )
    return errors
