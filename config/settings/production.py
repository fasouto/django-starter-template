from .base import *  # noqa: F403
from .base import env

DEBUG = False

# SECRET_KEY has a build-time fallback so collectstatic can run during
# the Railpack build phase (before env vars are injected).
# At runtime the real key is always required via the environment variable.
SECRET_KEY = env("SECRET_KEY", default="build-time-placeholder")

DATABASES = {
    "default": env.db("DATABASE_URL", default="sqlite:///placeholder"),
}
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)
DATABASES["default"]["CONN_HEALTH_CHECKS"] = True

# HOSTS
# Railway injects RAILWAY_PUBLIC_DOMAIN (e.g. "myapp.up.railway.app") for every
# service with a public domain. Use it so login/admin/forms work out of the box
# without hand-editing ALLOWED_HOSTS or CSRF_TRUSTED_ORIGINS.
# Add custom domains via the ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS variables.
RAILWAY_PUBLIC_DOMAIN = env("RAILWAY_PUBLIC_DOMAIN", default="")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[".railway.app"])
if RAILWAY_PUBLIC_DOMAIN and RAILWAY_PUBLIC_DOMAIN not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(RAILWAY_PUBLIC_DOMAIN)

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])
if RAILWAY_PUBLIC_DOMAIN and f"https://{RAILWAY_PUBLIC_DOMAIN}" not in CSRF_TRUSTED_ORIGINS:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RAILWAY_PUBLIC_DOMAIN}")

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

# Railway redirects HTTP -> HTTPS at the edge, so Django's own redirect is off
# (see SECURE_SSL_REDIRECT above). Silence the check that complains about it.
SILENCED_SYSTEM_CHECKS = ["security.W008"]
