from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect("accounts:signup")
    else:
        form = UserForm()
    
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)

def my_shop(request):
    return render(request, 'accounts/my_shop.html')