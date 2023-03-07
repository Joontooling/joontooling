from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path("", views.index, name="index"),
    path("notice/", views.notice, name="notice"),
    path("question/", views.question, name="question"),
    path("qna/", views.qna, name="qna"),
]
