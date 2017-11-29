from django.conf.urls import url, include
from .views import rent_all, do_search
from .views import rent_all, do_search, rent_details

urlpatterns = [
    url(r'^$', rent_all, name='rent'),
    url(r'^search/', do_search, name='search'),
    url(r'^(\d+)$', rent_details, name='rent_details'),
]