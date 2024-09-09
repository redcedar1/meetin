from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from common.models import Location
from geopy.distance import geodesic
import json

# 사용자의 현재 위치를 서버에 업데이트하는 API
@csrf_exempt
def update_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user  # 사용자가 로그인되어 있다고 가정
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # 사용자 위치를 저장하거나 업데이트
        Location.objects.update_or_create(
            user=user,
            defaults={'latitude': latitude, 'longitude': longitude, 'timestamp': timezone.now()}
        )

        return JsonResponse({'status': 'success', 'message': 'Location updated'})

# 일정 거리 내 사용자 조회 API
def nearby_users(request):
    latitude = float(request.GET.get('latitude'))
    longitude = float(request.GET.get('longitude'))
    distance = float(request.GET.get('distance', 1))  # 기본 반경은 1km

    current_location = (latitude, longitude)
    nearby_users = []

    # 모든 사용자 위치를 조회하고, 일정 거리 내 사용자만 필터링
    for location in Location.objects.all():
        user_location = (location.latitude, location.longitude)
        if geodesic(current_location, user_location).km <= distance:
            nearby_users.append({
                'user_id': location.user.id,
                'username': location.user.username,
                'latitude': location.latitude,
                'longitude': location.longitude,
                'timestamp': location.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            })

    return JsonResponse({'nearby_users': nearby_users})

def update_location_view(request):
    return render(request, 'update_location.html')

def nearby_users_view(request):
    return render(request, 'nearby_users.html')