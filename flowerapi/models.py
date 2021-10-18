from django.db import models

# Create your models here.

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=250)
    product_stock = models.IntegerField()
    product_price = models.FloatField()
    product_popularity = models.IntegerField()
    product_category = models.CharField(max_length=250)
 

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_time = models.DateTimeField(auto_now_add=True)
    order_product = models.CharField(max_length=250)
    order_quantity = models.IntegerField()
    order_subtotal = models.FloatField()
    order_total = models.FloatField()
 
   