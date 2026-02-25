from django.urls import path

from .views import home

app_name = "base"

urlpatterns = [
    path("", home, name="home"),
]
