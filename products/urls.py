from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:product_pk>/", views.detail, name="detail"), # 디테일 pk 값 인자로 받을 수 있도록 수정
    path("basket/", views.basket, name="basket"),
    path("order/", views.order, name="order"),
    path("order_done/", views.order_done, name="order_done"),
    path('product_create', views.product_create, name="product_create"),
    path('product_list/', views.product_list, name="product_list"),
]
