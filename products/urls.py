from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("products/detail/", views.detail, name="detail"),
    path("products/basket/", views.basket, name="basket"),
    path("products/order/", views.order, name="order"),
    path("products/order_done/", views.order_done, name="order_done"),
    path('products/product_create', views.product_create, name="product_create"),
    path('products/product_list/', views.product_list, name="product_list"),
]
