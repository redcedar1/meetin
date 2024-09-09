from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('common.urls')),
    path('kakaoapi/', include('kakaoapi.urls')),
    path('updatelocation/', include('updatelocation.urls'))
]