from django.shortcuts import render

# decorator csrf allows other domains to access my api methods
from django.views.decorators.csrf import csrf_exempt


# For parsing to json
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# import my data models and serializers
from flowerapi.models import Products, Orders
from flowerapi.serializers import ProductsSerializer, OrdersSerializer

# paginator
from django.core.paginator import Paginator, EmptyPage


from pprint import pprint as pp_pprint


# Create your views here.

# Adding index page
def index(request):
    return render(request, 'index.html')


# GET endpoint for products
@csrf_exempt
def productsApi(request,id=0):
    if request.method == 'GET':

        # Get all products
        products = Products.objects.all()

        # Get page number and size from url
        page_size = request.GET.get('size', 5)
        page_num = request.GET.get('page', 1)

        # URL name to use in template
        urlname = "products"

        one_product = ""

        if id != 0:
            
            # Get product by id
            product = Products.objects.filter(product_id = id)

            Category = ""

            # Get product Category
            for e in product:
               Category = e.product_category

            
            product_serializer = ProductsSerializer(product, many=True)

            one_product = product_serializer.data

            # Find related products
            products = Products.objects.filter(product_category = Category).order_by('-product_popularity')

            # Set page size to fit all related products
            page_size = len(products)


        products_serializer = ProductsSerializer(products, many=True)
    
        # Call paginator and give it json and page size
        p = Paginator(products_serializer.data, page_size)

        # if page does not exist, select page 1
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)


        context = {'items' : page, 'urlname' : urlname, 'pagesize' : page_size, 'one_product' : one_product}


        return render(request, 'index.html', context)


# GET endpoint for Orders
@csrf_exempt
def ordersApi(request,id=0):
    if request.method == 'GET':

        # Get all orders
        orders = Orders.objects.all()
        orders_serializer = OrdersSerializer(orders, many=True)

        # URL name to use in template
        urlname = "orders"

        # Get page number and size from url
        page_size = request.GET.get('size', 5)
        page_num = request.GET.get('page', 1)

        # Call paginator and give it json and page size
        p = Paginator(orders_serializer.data, page_size)

        # if page does not exist, select page 1
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)


        context = {'items' : page, 'urlname' : urlname, 'pagesize' : page_size}

        return render(request, 'index.html', context)


    