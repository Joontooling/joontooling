# Generated by Django 3.2.13 on 2023-03-16 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_alter_notice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='type',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100),
        ),
    ]
