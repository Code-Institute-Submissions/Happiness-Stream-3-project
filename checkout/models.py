from django.db import models
from buy.models import Buy
from rent.models import Rent
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    buy = models.ForeignKey(Buy, null=False)
    rent = models.ForeignKey(Rent, null=False)
    quantity = models.IntegerField(blank=False)
    
    # what aboout rent
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
