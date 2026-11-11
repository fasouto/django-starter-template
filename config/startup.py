from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

PLACEHOLDER_SECRET_KEYS = {
    "django-insecure-dev-key-change-me",
    "build-time-placeholder",
    "change-me-to-a-random-string",
}


def require_real_secret_key():
    if not settings.DEBUG and settings.SECRET_KEY in PLACEHOLDER_SECRET_KEYS:
        raise ImproperlyConfigured(
            "SECRET_KEY is a placeholder, so the app refuses to start. "
            "Set the SECRET_KEY variable on your Railway service (or environment) "
            "to a long random value, for example the output of: openssl rand -hex 32"
        )
