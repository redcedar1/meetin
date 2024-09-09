from django.urls import path
from . import views

urlpatterns = [
    path('update-location/', views.update_location_view, name='update_location_view'),
    path('nearby-users/', views.nearby_users_view, name='nearby_users_view'),
]
