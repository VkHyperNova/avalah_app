from rest_framework import serializers
from FlowerApp.models import Products, Orders


# Serializer to convert querysets to native Python datatypes

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=('ProductId','ProductName','ProductStock','ProductPrice')

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=('Time','Product','Quantity','OrderSubtotal','OrderTotal')