"""
Project main settings file. These settings are common to the project 
if you need to override something do it in local.pt
"""

from os.path import abspath, basename, dirname, join, normpath
from sys import path


## SITE PATH
# Build paths inside the project like this: join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(__file__))
path.append(BASE_DIR)


## SITE SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# https://docs.djangoproject.com/en/1.8/ref/settings/#installed-apps
INSTALLED_APPS = [
    'flat', # django-flat-theme must be BEFORE contrib.admin

    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'django.contrib.staticfiles',

    # Third party apps
    'debug_toolbar',
    'compressor',

    # Local apps
    'base',
]

# https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#using-bcrypt-with-django
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

## DEBUG SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#debug
DEBUG = False

# https://docs.djangoproject.com/en/1.8/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG

# https://docs.djangoproject.com/en/1.8/ref/settings/#internal-ips
INTERNAL_IPS = ('127.0.0.1')


## DATABASE SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


## LOCALE SETTINGS
# Local time zone for this installation. 
# https://docs.djangoproject.com/en/1.8/ref/settings/#time-zone
TIME_ZONE = 'America/Los_Angeles'

# https://docs.djangoproject.com/en/1.8/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-tz
USE_TZ = True


## MEDIA AND STATIC SETTINGS
# Absolute filesystem path to the directory that will hold user-uploaded files.
# https://docs.djangoproject.com/en/1.8/ref/settings/#media-root
MEDIA_ROOT = join(BASE_DIR, 'public/media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a trailing slash.
# https://docs.djangoproject.com/en/1.8/ref/settings/#media-url
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# https://docs.djangoproject.com/en/1.8/ref/settings/#static-root
STATIC_ROOT = join(BASE_DIR, 'public/static')

# URL prefix for static files.
# https://docs.djangoproject.com/en/1.8/ref/settings/#static-url
STATIC_URL = '/static/'

# Additional locations of static files
# https://docs.djangoproject.com/en/1.8/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

# https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

## TEMPLATE SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
]

# https://docs.djangoproject.com/en/1.8/ref/settings/#template-dirs
TEMPLATE_DIRS = [
    join(BASE_DIR, 'templates'),
]

# https://docs.djangoproject.com/en/1.8/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


## URL SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#root-urlconf.
ROOT_URLCONF = '{{ project_name }}.urls'


## MIDDLEWARE SETTINGS
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


## WSGI SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#wsgi-application
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


## NOTIFICATIONS AND LOGGING
# A tuple that lists people who get code error notifications.
# https://docs.djangoproject.com/en/1.8/ref/settings/#admins
ADMINS = (
    ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

LOGGING = {
    'version': 1,
    'loggers': {
        '{{ project_name }}': {
            'level': "DEBUG"
        }
    }
}


## DJANGO DEBUG TOOLBAR SETTINGS
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'HIDE_DJANGO_SQL': True,
    'TAG': 'body',
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': True,
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
)
