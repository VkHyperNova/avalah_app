from django.conf.urls import url
from flowerapi import views

urlpatterns = [
    
    url(r'^products$', views.GetProducts, name="products"),
    url(r'^products/([0-9]+)$', views.GetProductsById, name="products"),

    url(r'^orders$', views.GetOrders, name="orders"),
    
]