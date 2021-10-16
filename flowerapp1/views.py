from django.shortcuts import render

# decorator csrf allows other domains to access my api methods
from django.views.decorators.csrf import csrf_exempt

# For parsing to json
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# import my data models and serializers
from flowerapp.models import Products, Orders
from flowerapp.serializers import ProductsSerializer, OrdersSerializer

# Create your views here.

# Adding index page
def index(request):
    return render(request, "index.html")


# GET, POST, PUT, DELETE for Products
@csrf_exempt
def productsApi(request,id=0):
    if request.method == 'GET':

        products = Products.objects.all()
        products_serializer = ProductsSerializer(products, many=True)

        return JsonResponse(products_serializer.data, safe=False)

    elif request.method == 'POST':

        product_data = JSONParser().parse(request)
        products_serializer = ProductsSerializer(data=product_data)

        if products_serializer.is_valid():

            products_serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        
        product_data = JSONParser().parse(request)
        product = Products.objects.get(product_id = product_data['product_id'])
        products_serializer = ProductsSerializer(product, data = product_data)

        if products_serializer.is_valid():

            products_serializer.save()

            return JsonResponse("Updated Successfully", safe = False)

        return JsonResponse("Failed to Update")

    elif request.method == 'DELETE':

        product = Products.objects.get(product_id = id)
        product.delete()

        return JsonResponse("Deleted Successfully", safe = False)


# GET, POST and DELETE for Orders
@csrf_exempt
def ordersApi(request,id=0):
    if request.method == 'GET':

        orders = Orders.objects.all()
        orders_serializer = OrdersSerializer(orders, many=True)

        return JsonResponse(orders_serializer.data, safe=False)

    elif request.method == 'POST':

        order_data = JSONParser().parse(request)
        orders_serializer = OrdersSerializer(data=order_data)

        if orders_serializer.is_valid():

            orders_serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
        
    elif request.method == 'PUT':
        
        order_data = JSONParser().parse(request)
        order = Orders.objects.get(order_id = order_data['order_id'])
        orders_serializer = OrdersSerializer(order, data = order_data)

        if orders_serializer.is_valid():

            orders_serializer.save()

            return JsonResponse("Updated Successfully", safe = False)

        return JsonResponse("Failed to Update")


    elif request.method == 'DELETE':

        order = Products.objects.get(order_id = id)
        order.delete()

        return JsonResponse("Deleted Successfully", safe = False)