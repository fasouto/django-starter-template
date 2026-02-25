from .base import *  # noqa: F403
from .base import env

DEBUG = False

# SECRET_KEY has a build-time fallback so collectstatic can run during
# the Docker/Railpack build phase (before env vars are injected).
# At runtime the real key is always required via the environment variable.
SECRET_KEY = env("SECRET_KEY", default="build-time-placeholder")

DATABASES = {
    "default": env.db("DATABASE_URL", default="sqlite:///placeholder"),
}

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[".railway.app"])

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

# SECURITY
# Railway terminates SSL at the proxy; internal traffic is HTTP.
# Let the proxy handle HTTPS redirection, not Django.
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=False)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
