# Generated by Django 3.2.13 on 2023-03-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230302_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image_main',
            field=models.ImageField(default='/media/product/default_img.jpg', null=True, upload_to='images/'),
        ),
    ]