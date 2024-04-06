from django.urls import path
from .views import common_views

app_name = "common"

urlpatterns = [
    path('', common_views.index, name="index"),
]