from django.urls import path
from . import views

urlpatterns = [
    path('update-location/', views.update_location_view, name='update_location_view'),
    path('nearby-users/', views.nearby_users_view, name='nearby_users_view'),
    path('api/update-location/', views.update_location, name='update_location'),
    path('api/nearby-users/', views.nearby_users, name='nearby_users'),
]
