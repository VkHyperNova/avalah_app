from rest_framework import serializers
from flowerapi.models import Products, Orders


# Serializer to convert querysets to native Python datatypes

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=('product_id','product_name','product_stock','product_price', 'product_popularity', 'product_category')

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=('order_id','order_time','order_product','order_quantity','order_subtotal','order_total')