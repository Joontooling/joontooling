from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    price = models.IntegerField()
    quantity = models.IntegerField()
    point = models.IntegerField()
    serial = models.CharField(max_length=80)
    delivery = models.IntegerField()
    image_main = models.ImageField(default='media/product/default_img.jpg', upload_to="images/", null=True)

class ProductsInfo(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="product_image"
    )
    image_sub = models.ImageField(upload_to="images/", blank=True, null=True)