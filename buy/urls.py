from django.conf.urls import url, include
from .views import buy_all, do_search
from .views import buy_all, do_search, buy_details

urlpatterns = [
    url(r'^$', buy_all, name='buy'),
    url(r'^search/', do_search, name='search'),
    url(r'^(\d+)$', buy_details, name='buy_details'),
]