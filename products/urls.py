from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
    path("basket/", views.basket, name="basket"),
    path('product_create', views.product_create, name="product_create"),
]
