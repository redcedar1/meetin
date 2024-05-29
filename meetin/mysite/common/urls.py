from django.urls import path
from .views import common_views

app_name = "common"

urlpatterns = [
    path('', common_views.index, name="index"),
    path('home/', common_views.home, name='home'),
    path('menu/', common_views.menu,name='menu'),
]