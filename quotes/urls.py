"""
URL Configuration for quotes
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the quotes app here
    url(r'^$', views.home, name='home'),
    url(r'^(?P<stock_symbol>.*$)', views.symbol, name='stock_symbol'),
]
