# pages/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):  # nuevo
    template_name = "about.html"