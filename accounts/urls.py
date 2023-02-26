from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("my_shop/", views.my_shop, name="my_shop"),
    path("my_likes/", views.my_likes, name="my_likes"),
]