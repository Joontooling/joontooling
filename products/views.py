from django.shortcuts import render, redirect
from .form import ProductsForm, ProductsInfoForm
from .models import Products, ProductsInfo


def index(request):
    products = Products.objects.all().order_by("-pk")

    context = {
        "products" : products
    }


    return render(request, "products/index.html", context)

# 디테일 데이터 넘겨주는 값 수정
def detail(request, product_pk):
    product = Products.objects.get(pk=product_pk)
    imgproducts = ProductsInfo.objects.filter(product=product_pk)

    point_ = (product.price // product.point) // 100

    # 메인 사진 리스트 별도
    Images = [product.image_main1, product.image_main2, product.image_main3, product.image_main4, product.image_main5]

    context = {
        "product" : product,
        "imgproducts" : imgproducts,
        "point_": point_,
        "Images" : Images,
    }

    return render(request, 'products/detail.html', context)


def basket(request):
    return render(request, 'products/basket.html')

def order(request):
    return render(request, 'products/order.html')

def order_done(request):
    return render(request, 'products/order_done.html')


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

def product_list(request):
    return render(request, "products/product_list.html")


def terms(request):
    return render(request, "products/terms.html")

def personal_info(request):
    return render(request, "products/personal_info.html")

def use_info(request):
    return render(request, "products/use_info.html")