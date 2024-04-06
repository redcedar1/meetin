from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('main/', include('common.urls')),
    path('kakaopay/', include('kakaopay.urls')),
    path('room/', include('room.urls')),
]