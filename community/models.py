from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class QnA(models.Model):
    Question = models.IntegerField(primary_key=True)
    TYPE_CHOICES = []   # 추후 수정
    LOCK_CHOICES = [("Y", "Yes"), ("N", "No")]
    user_id = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    title = models.CharField(max_length=80)
    type = models.CharField(choices=TYPE_CHOICES, max_length=80)
    content = models.TextField()
    b_pwd = models.IntegerField()   # 추후 수정
    date = models.DateTimeField()
    p_image = models.ImageField(upload_to="images/", null=True)
    lock_flag = models.CharField(choices=LOCK_CHOICES, max_length=80)


# 공지사항 테스트용
class Notice(models.Model):
    no = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    NOTICE_TYPE_CHOICES = [
        ("1", "1"), 
        ("2", "2"),
        ("3", "3"),
        ]
    type = models.CharField(choices=NOTICE_TYPE_CHOICES, max_length=100)
    date = models.DateField()