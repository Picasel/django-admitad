from django.apps import apps


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
