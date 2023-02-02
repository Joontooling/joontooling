from django import forms
from .models import Products, ProductsInfo

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ["name", "category", "price", "quantity", "point", "serial", "delivery",]
        labels = {
            "name" : "상품명", 
            "category" : "상품 분류",
            "price" : "상품가격",
            "quantity" : "재고량",
            "point" : "적립금",
            "serial" : "고유번호",
            "delivery" : "배송비",
        }

class ProductsInfoForm(forms.ModelForm):
    image = forms.ImageField(
        label='상품이미지',
        widget=forms.ClearableFileInput(attrs={'multiple':True}),
    )
    class Meta:
        model = ProductsInfo
        fields = ('image_main', "image_sub",)
        label = {
            'image_main' : "상품 메인 사진",
            'image_sub' : "상품 상세 사진",
        }