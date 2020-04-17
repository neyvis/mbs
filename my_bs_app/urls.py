"""my_bs_app URL Configuration

"""
from django.urls import path

from .views import home

urlpatterns = [
    path("", home, name='home'),
]
