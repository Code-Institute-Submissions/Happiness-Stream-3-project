from django.conf.urls import url, include
from .views import buy_all, do_search
from .views import buy_all, do_search, buy_details
from checkout.views import buy_checkout

urlpatterns = [
    url(r'^$', buy_all, name='buy'),
    # url(r'^search/$', do_search, name='search'),
    # url(r'^(\d+)/$', buy_details, name='buy_details'),
    # url(r'^(\d+)/checkout$', buy_checkout, name='buy_checkout'),
]