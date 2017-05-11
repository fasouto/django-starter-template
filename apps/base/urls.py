"""urlconf for the base application"""

from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^home$', index, name='index'),
]
