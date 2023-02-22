from django.shortcuts import render, redirect
from .form import ProductsForm, ProductsInfoForm
from .models import Products, ProductsInfo


# 템플릿 확인용
def detail(request):
    return render(request, 'products/detail.html')

def index(request):

    return render(request, "products/index.html")

def product_create(request):
    if request.method == "POST":
        create_form = ProductsForm(request.POST, request.FILES)
        product_images = request.FILES.getlist("image")
        if create_form.is_valid():
            product = create_form.save()
            for img in product_images:
                ProductsInfoForm.objects.create(product=product, image_main=img )
            return redirect("/")
    else:
        create_form = ProductsForm()
        product_image_form = ProductsInfoForm()


    context = {
        "create_form": create_form,
        "product_image_form" : product_image_form,
    }

    return render(request, "products/product_create.html", context)

