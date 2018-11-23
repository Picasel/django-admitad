from django.core.checks import register

SUPPORTED_DJANGO_VERSIONS = ['2.1', ]
SUPPORTED_PYTHON_VERSIONS = ['3.7', ]


@register()
def django_version_checks(app_configs, **kwargs):
    # TODO
    return


@register()
def python_version_checks(app_configs, **kwargs):
    # TODO
    return
