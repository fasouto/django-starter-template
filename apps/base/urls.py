"""urlconf for the base application"""

from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
]
