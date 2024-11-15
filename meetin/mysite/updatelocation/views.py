from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from common.models import Location, Info
from geopy.distance import geodesic
import json, requests

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
    access_token = request.session.get("access_token", None)
    if access_token is None:  # 로그인 안돼있으면
        return render(request, "kakaologin.html")  # 로그인 시키기

    # 현재 로그인된 사용자 정보 가져오기
    account_info = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"}
    ).json()
    kakao_id = account_info.get("id")
    try:
        user_info = Info.objects.get(kakao_id=kakao_id)
    except Info.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    # latitude와 longitude 값 가져오기
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    distance = float(request.GET.get('distance', 100))  # 기본 반경은 100km

    # 유효성 검사: latitude와 longitude가 없으면 오류 반환
    if latitude is None or longitude is None:
        return JsonResponse({'error': 'Missing latitude or longitude'}, status=400)

    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return JsonResponse({'error': 'Invalid latitude or longitude values'}, status=400)

    # 사용자 위치 정보 업데이트 또는 생성
    location, created = Location.objects.update_or_create(
        user=user_info,  # 조건: 현재 사용자의 위치
        defaults={'latitude': latitude, 'longitude': longitude}  # 값 업데이트
    )

    current_location = (latitude, longitude)
    nearby_users = []

    # 사용자 위치 필터링: 일정 거리 내 사용자만 조회
    locations = Location.objects.all()
    for location in locations:
        user_location = (location.latitude, location.longitude)
        calculated_distance = geodesic(current_location, user_location).km

        # 지정한 거리 내에 있는 사용자만 필터링
        if calculated_distance <= distance:
            nearby_users.append({
                'user_id': location.user.id,
                'username': location.user.kakao_id,
                'age': location.user.age,
                'school': location.user.school,
                'major': location.user.major,
                'mbti': location.user.mbti,
                'hobby': location.user.hobby,
                'latitude': location.latitude,
                'longitude': location.longitude,
                'timestamp': location.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'distance': round(calculated_distance, 2)  # 사용자와의 거리 추가
            })

    return JsonResponse({'nearby_users': nearby_users})

def update_location_view(request):
    return render(request, 'update_location.html')

def nearby_users_view(request):
    return render(request, 'nearby_users.html')