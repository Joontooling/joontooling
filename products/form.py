from django import forms
from .models import Products, ProductsInfo

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ["name", "category", "price", "quantity", "point", "serial", "delivery","image_main"]
        labels = {
            "name" : "상품명", 
            "category" : "상품 분류",
            "price" : "상품가격",
            "quantity" : "재고량",
            "point" : "적립금",
            "serial" : "고유번호",
            "delivery" : "배송비",
            "image_main" : "메인 사진",
        }

class ProductsInfoForm(forms.ModelForm):
    image = forms.ImageField(
        label='상품 상세 사진',
        widget=forms.ClearableFileInput(attrs={'multiple':True}),
    )
    class Meta:
        model = ProductsInfo
        fields = ['image_sub',]
        labels = {
            'image_sub' : "상품 상제 사진",
        }