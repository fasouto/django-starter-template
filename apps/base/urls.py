"""urlconf for the base application"""

from django.conf.urls import url

from .views import home


urlpatterns = [
    url(r'^$', home, name='home'),
]
