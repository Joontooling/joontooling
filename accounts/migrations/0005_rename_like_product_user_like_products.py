# Generated by Django 3.2.13 on 2023-03-22 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_like_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='like_product',
            new_name='like_products',
        ),
    ]
