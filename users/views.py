from django.shortcuts import render, redirect
from .forms import UserForm, UserCustomChangeForm, CustomPasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
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
        return render(request, "users/signup.html", context)
    
    else:
        return redirect("products:index")

def login(request):

    if not request.user.is_authenticated:
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

        return render(request, 'users/login.html', context)

    else:
        return redirect("products:index")

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
                return redirect('users:my_shop', request.user.pk)
        else:
            change_form = UserCustomChangeForm(instance=request.user)
            
        password_form = CustomPasswordChangeForm(request.user)
    
        context = {
            'change_form': change_form,
            'password_form': password_form,
        }

        return render(request, 'users/update.html', context)

    else:
        return redirect('products:index')

@login_required
def password_update(request):
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(request.POST, request.user)
        if password_form.is_valid():
            user = password_form.save()
            auth_login(request, user)
            return redirect('users:update', request.user.pk)
    else:
        password_form = CustomPasswordChangeForm(request.user)

    context = {
        'password_form': password_form,
    }
    
    return render(request, 'users/password.html', context)

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

    return render(request, 'users/my_shop.html', context)

# 관심상품
def my_likes(request, pk):
    users = get_user_model().objects.get(pk=pk)
    like_product = users.like_products.all()
    if request.method == "POST":
        selected = request.POST.getlist("answer[]")
        for product in selected:
            for i in range(len(like_product)):
                if int(product) == like_product[i].pk:
                    like_product[i].delete()
    context = {"users" : users}
    return render(request, 'users/my_likes.html', context)

def my_posting(request, pk):
    return render(request, 'users/my_posting.html')

def agreement1(request):
    return render(request, 'users/agreement1.html')

def agreement2(request):
    return render(request, 'users/agreement2.html')

def agreement3(request):
    return render(request, 'users/agreement3.html')