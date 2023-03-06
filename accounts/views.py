from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login


# Create your views here.
def signup(request):
    if request.method == "POST":

        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            user_sign_up = form.save()
            auth_login(request, user = user_sign_up)
            return redirect("products:index")
    else:
        form = UserForm()
    
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)

def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            print("로그인 성공")
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'products:index')
    
    else:
        print("로그인 실")
        form = AuthenticationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/login.html', context)

def my_shop(request):
    return render(request, 'accounts/my_shop.html')

def my_likes(request):
    return render(request, 'accounts/my_likes.html')

def my_posting(request):
    return render(request, 'accounts/my_posting.html')