from django.shortcuts import render, redirect
from .forms import UserForm, UserCustomChangeForm, CustomPasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required


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
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'products:index')
    
    else:
        form = AuthenticationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('products:index')

@login_required
def update(request, pk):

    if request.user.pk == pk:
    
        if request.method == 'POST':
            change_form = UserCustomChangeForm(request.POST, request.FILES, instance=request.user)
            if change_form.is_valid():
                change = change_form.save()
                auth_login(request, user=change)
                return redirect('accounts:my_shop', request.user.pk)
        else:
            change_form = UserCustomChangeForm(instance=request.user)
    
        context = {
        'change_form': change_form,
        }

        return render(request, 'accounts/update.html', context)
  
    else:
        return redirect('products:index')

@login_required
def password_update(request):
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(request.POST, request.user)
        if password_form.is_valid():
            user = password_form.save()
            auth_login(request, user)
            return redirect('accounts:update', request.user.pk)
    else:
        password_form = CustomPasswordChangeForm(request.user)

    context = {
        'password_form': password_form,
    }
    
    return render(request, 'accounts/password.html', context)

@login_required
def delete(request, pk):
    if request.user.pk == pk:
        request.user.delete()
    return redirect('products:index')

@login_required
def my_shop(request, pk):

    if request.user.pk == pk:

        context = {
            'user_pk' : pk,
        }

    return render(request, 'accounts/my_shop.html', context)

def my_likes(request, pk):
    return render(request, 'accounts/my_likes.html')

def my_posting(request, pk):
    return render(request, 'accounts/my_posting.html')