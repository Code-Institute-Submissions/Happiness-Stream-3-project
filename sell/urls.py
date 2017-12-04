from django.conf.urls import url, include
from .views import create_for_sale_ad, do_search


urlpatterns = [
    url(r'^create$', create_for_sale_ad, name='create_for_sale_ad'),
    url(r'^search/', do_search, name='search'),
]