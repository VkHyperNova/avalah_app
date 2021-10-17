from django.conf.urls import url
from flowerapi import views

urlpatterns = [
    
    url(r'^products$', views.productsApi, name="products"),
    url(r'^products/([0-9]+)$', views.productsApi, name="products"),

    url(r'^orders$', views.ordersApi, name="orders"),
    url(r'^orders/([0-9]+)$', views.ordersApi, name="orders")
]