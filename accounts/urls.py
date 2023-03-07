from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/<int:pk>/", views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('password_update/', views.password_update, name='password_update'),
    path("my_shop/<int:pk>/", views.my_shop, name="myshop"),
    path("my_likes/<int:pk>/", views.my_likes, name="mylikes"),
    path("my_posting/<int:pk>/", views.my_posting, name="myposting"),
]