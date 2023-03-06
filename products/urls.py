from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("products/detail/<int:product_pk>/", views.detail, name="detail"), # 디테일 pk 값 인자로 받을 수 있도록 수정
    path("products/basket/", views.basket, name="basket"),
    path("products/order/", views.order, name="order"),
    path("products/order_done/", views.order_done, name="order_done"),
    path('products/product_create', views.product_create, name="product_create"),
    path('products/product_list/', views.product_list, name="product_list"),
]
