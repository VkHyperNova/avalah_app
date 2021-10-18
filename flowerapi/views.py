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


# GET endpoint for products
@csrf_exempt
def productsApi(request,id=0):

        # Get all products
        products = Products.objects.all()

        # Get page number and size from url
        page_size = request.GET.get('size', 5)
        page_num = request.GET.get('page', 1)

        # URL name to use in template
        urlname = "products"

        product_by_id = ""

        msg = ""

        if id != 0:
            
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
          
            product_serializer = ProductsSerializer(product, many=True)

            product_by_id = product_serializer.data

            # Find related products
            products = Products.objects.filter(product_category = Category).order_by('-product_popularity')

            # Set page size to fit all related products
            page_size = len(products)


        products_serializer = ProductsSerializer(products, many=True)

        # Call paginator and give it json and page size
        p = Paginator(products_serializer.data, page_size)

        # if page does not exist, select page 1
        try:
            items = p.page(page_num)
        except EmptyPage:
            items = p.page(1)

        context = {'items' : items, 'urlname' : urlname, 'product_by_id' : product_by_id, 'msg' : msg}

        return render(request, 'index.html', context)

# GET endpoint for Orders
@csrf_exempt
def ordersApi(request):

        # Get all orders
        orders_serializer = OrdersSerializer(Orders.objects.all(), many=True)

        # URL name to use in template
        urlname = "orders"

        # Get page number and size from url
        page_size = request.GET.get('size', 5)
        page_num = request.GET.get('page', 1)

        # Call paginator and give it json and page size
        p = Paginator(orders_serializer.data, page_size)

        # if page does not exist, select page 1
        try:
            items = p.page(page_num)
        except EmptyPage:
            items = p.page(1)

        context = {'items' : items, 'urlname' : urlname}

        return render(request, 'index.html', context)


    