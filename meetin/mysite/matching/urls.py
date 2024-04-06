from django.urls import path
from .views import matching_views

app_name = "matching"

urlpatterns = [
    path('', matching_views.index, name="index"),
]