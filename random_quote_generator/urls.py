"""random_quote_generator URL Configuration"""
from django.urls import path

from main.views import MainTemplateView


urlpatterns = [
    path('', MainTemplateView.as_view(), name='main')
]
