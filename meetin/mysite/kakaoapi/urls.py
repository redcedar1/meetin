from django.urls import path
from . import views

app_name = "kakaoapi"

urlpatterns = [
    path('', views.index),
]