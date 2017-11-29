from django.db import models

class Rent(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
        
class RentImage(models.Model):
    rent= models.ForeignKey(Rent, related_name='images')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return str(self.image)