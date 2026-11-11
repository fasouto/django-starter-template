import os

from django.core.asgi import get_asgi_application

from config.startup import require_real_secret_key

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_asgi_application()

require_real_secret_key()
