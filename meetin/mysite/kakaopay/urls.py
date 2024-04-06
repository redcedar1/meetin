from django.urls import path
from .views import kakaopay_views

app_name = "kakaopay"

urlpatterns = [
    path('', kakaopay_views.index, name="index"),
]