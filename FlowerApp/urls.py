from django.conf.urls import url
from FlowerApp import views

urlpatterns = [
    url(r'^product$', views.productsApi),
    url(r'^product/([0-9]+)$', views.productsApi),

    url(r'^order$', views.ordersApi),
    url(r'^order/([0-9]+)$', views.ordersApi)
]