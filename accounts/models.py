from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # password
    # group
    # user_permission
    # is_staff
    # is_active
    # is_superuer

    type_choice = (
        ("개인회원", "개인회원"),
        ("개인사업자", "개인사업자"),
        ("법인사업자", "법인사업자"),
    )

    address = models.CharField(max_length=100)

    # 전화번호 지정
    phone_num_regex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone_number = models.CharField(max_length=11, validators= [phone_num_regex], null=True)

    birth = models.DateTimeField(null=True)
    user_type = models.CharField(max_length=20, choices=type_choice)

    # user 타입에 따라 밑에 있는 필드들을 넣어야 한
    company = models.CharField(max_length=50, null=True)
    per_company_number = models.CharField(max_length=30, null=True)
    company_number = models.IntegerField(null=True)
    point = models.IntegerField(null=True)

