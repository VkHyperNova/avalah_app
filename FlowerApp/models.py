from django.db import models

# Create your models here.

class Products(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=500)
    ProductStock = models.IntegerField()
    ProductPrice = models.FloatField()

class Orders(models.Model):
    Time = models.TimeField()
    Product = models.CharField(max_length=500)
    Quantity = models.IntegerField()
    OrderSubtotal = models.FloatField()
    OrderTotal = models.FloatField()