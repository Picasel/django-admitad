from django.apps import apps

try:
    import urlparse
    from urllib import urlencode
except ImportError:  # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode


def add_params_to_url(url, params):
    """
    Applies params to url
    """
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)

    return urlparse.urlunparse(url_parts)


def is_model_registered(app_label, model_name):
    """
    Checks whether a given model is registered. This is used to only
    register admitad models if they aren't overridden by a forked app.
    """
    try:
        apps.get_registered_model(app_label, model_name)
    except LookupError:
        return False
    else:
        return True
