# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView  # nuevo

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),  # nuevo
    path("", HomePageView.as_view(), name="home"),
]