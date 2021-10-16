from django.conf.urls import url
from flowerapp import views

urlpatterns = [
    
    url(r'^products$', views.productsApi),
    url(r'^products/([0-9]+)$', views.productsApi),

    url(r'^orders$', views.ordersApi),
    url(r'^orders/([0-9]+)$', views.ordersApi)
]