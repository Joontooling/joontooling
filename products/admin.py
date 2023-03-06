from django.contrib import admin
from .models import Products, ProductsInfo
# Register your models here.

# admin 상품 등록

class AddInfoImage(admin.StackedInline):
    model = ProductsInfo

class InfoProductAdmin(admin.ModelAdmin):
    inlines = [AddInfoImage,] # 상세 설명 이미지 등록 모델 인라인 추가 설정

admin.site.register(Products, InfoProductAdmin)