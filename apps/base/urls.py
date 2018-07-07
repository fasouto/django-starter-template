"""urlconf for the {{ project_name }} application"""

from django.urls import path

from .views import home


urlpatterns = [
    path('', home, name='home'),
]
