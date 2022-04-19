from email.policy import default
from django.db import models

# Create your models here.

class Distributor(models.Model):
    distributor_name = models.CharField(max_length=50, unique=True)
    distributor_description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.distributor_name

class Product(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, unique=True)
    product_description = models.CharField(max_length=200)
    product_price = models.FloatField(max_length=50)
    product_qt = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name