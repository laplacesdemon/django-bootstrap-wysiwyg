from django.conf import settings


def setting(name, default=None):
    """returns the setting value or default if not exists"""
    return getattr(settings, name, default)
