# Generated by Django 3.2.13 on 2023-02-09 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('Question', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('type', models.CharField(choices=[], max_length=80)),
                ('content', models.TextField()),
                ('b_pwd', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('p_image', models.ImageField(null=True, upload_to='images/')),
                ('lock_flag', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=80)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
