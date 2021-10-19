from django.shortcuts import render

# decorator csrf allows other domains to access my api methods
from django.views.decorators.csrf import csrf_exempt

# import my data models and serializers
from flowerapi.models import Products, Orders
from flowerapi.serializers import ProductsSerializer, OrdersSerializer

# paginator
from django.core.paginator import Paginator, EmptyPage

# Create your views here.

# Adding index page
def index(request):
    return render(request, 'index.html')

# Get product by id
@csrf_exempt
def GetProductsById(request, id):

    # URL name to use in template
    urlname = "products"

    msg = ""

    # Check if id exist in db
    if Products.objects.filter(product_id = id).exists():
        # Get product by id
        product = Products.objects.filter(product_id = id)
    else:
        msg = "ID: " + id + " does not exist in db"
        # Set product id to 1
        product = Products.objects.filter(product_id = 1)

    Category = ""

    # Get product Category
    for e in product:
        Category = e.product_category

    # Serialize selected product
    product_serializer = ProductsSerializer(product, many=True)

    # Find related products and exclude selected product
    Related_products = Products.objects.filter(product_category = Category).exclude(product_id = id).order_by('-product_popularity')

    # Serialize Related products
    products_serializer = ProductsSerializer(Related_products, many=True)

    # Paginate Related products
    items = Paginate(request, products_serializer.data) 

    # Get the page size from url
    page_size = request.GET.get('size', 5)

    context = {'items' : items, 'urlname' : urlname, 'product' : product_serializer.data, 'msg' : msg, 'id' : id, 'page_size' : page_size}

    return render(request, 'index.html', context)




# Get all products
@csrf_exempt
def GetProducts(request):

    # URL name to use in template
    urlname = "products"

    # Serialize all products
    products_serializer = ProductsSerializer(Products.objects.all(), many=True)

    # Paginate
    items = Paginate(request, products_serializer.data) 

    context = {'items' : items, 'urlname' : urlname}

    return render(request, 'index.html', context)

# GET all orders
@csrf_exempt
def GetOrders(request):

    # URL name to use in template
    urlname = "orders"

    # Get all orders and serialize
    orders_serializer = OrdersSerializer(Orders.objects.all(), many=True)

    # Paginate
    items = Paginate(request, orders_serializer.data)

    context = {'items' : items, 'urlname' : urlname}

    return render(request, 'index.html', context)


def Paginate(request, data):

    # Get page number and size from url
    page_num = request.GET.get('page', 1)
    page_size = request.GET.get('size', 5)

    # Call paginator and give it json and page size
    p = Paginator(data, page_size)

    # if page does not exist, select page 1
    try:
        items = p.page(page_num)
    except EmptyPage:
        items = p.page(1)

    return items