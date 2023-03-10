import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    price = models.IntegerField()
    quantity = models.IntegerField()
    point = models.IntegerField()
    serial = models.CharField(max_length=80)
    delivery = models.IntegerField()
    image_main1 = models.ImageField(default='default_img.jpg', upload_to="images/", null=True) # 이미지 경로 및 기본 이미지 변경
    image_main2 = models.ImageField(default='default_img.jpg', upload_to="images/", null=True)
    image_main3 = models.ImageField(default='default_img.jpg', upload_to="images/", null=True)
    image_main4 = models.ImageField(default='default_img.jpg', upload_to="images/", null=True)
    image_main5 = models.ImageField(default='default_img.jpg', upload_to="images/", null=True)

    # admin 사이트에서 타이틀명 변경 되는 부분 수정
    def __str__(self):
        return self.name
    
    def summary(self):
        return self.body[:100]

class ProductsInfo(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="product_image"
    )
    image_sub = models.ImageField(upload_to="images/", blank=True, null=True)