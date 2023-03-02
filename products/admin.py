from django.contrib import admin
from .models import Products, ProductsInfo
# Register your models here.

class AddInfoImage(admin.StackedInline):
    model = ProductsInfo

class InfoProductAdmin(admin.ModelAdmin):
    inlines = [AddInfoImage,]

admin.site.register(Products, InfoProductAdmin)