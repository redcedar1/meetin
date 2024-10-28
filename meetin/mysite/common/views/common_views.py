import requests
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework import status
from rest_framework.views import APIView

from ..models import Info, womenInfo, menInfo, matchingInfo


@csrf_exempt
def index(request):
   return redirect("/home")


@csrf_exempt
def home(request):
    logged = 0
    access_token = request.session.get("access_token", None)

    if access_token:
        logged = 1
        account_info = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"}
        ).json()

        kakao_id = account_info.get("id")
        user_info = Info.objects.filter(kakao_id=kakao_id).first()

    context = {'logged': logged}
    return render(request, "home.html", context)


@csrf_exempt
def menu(request):
    return render(request, "menu.html")


def kakaologin(request):
    access_token = request.session.get("access_token", None)

    if access_token:
        account_info = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"}
        ).json()

        kakao_id = account_info.get("id")

        if kakao_id:
            user_profile, created = Info.objects.get_or_create(kakao_id=kakao_id)
            if created:
                print(f"새로운 Info 레코드 생성: {user_profile}")
            else:
                print(f"기존 Info 레코드 조회: {user_profile}")

            request.session["user_profile"] = kakao_id
            return redirect("/home")
        else:
            print("카카오 사용자 ID를 가져오는 데 실패했습니다.")
            return redirect("/kakaologin/")

    return render(request, "kakaologin.html")


def kakaoLoginLogic(request):
    _restApiKey = 'd37e3286aa4a1b7e3a2c084309f70d72'
    _redirectUrl = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)


def kakaoLoginLogicRedirect(request):
    code = request.GET.get('code')
    _restApiKey = 'd37e3286aa4a1b7e3a2c084309f70d72'
    _redirectUri = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    token_url = "https://kauth.kakao.com/oauth/token"

    response = requests.post(
        token_url,
        data={
            "grant_type": "authorization_code",
            "client_id": _restApiKey,
            "redirect_uri": _redirectUri,
            "code": code,
        },
    )

    access_token = response.json().get("access_token")
    if access_token:
        request.session["access_token"] = access_token
        print("Access token 저장 성공:", access_token)
        return redirect("/kakaologin")
    else:
        print("Access token 발급 실패:", response.json())
        return redirect("/kakaologin/")


def kakaoLogout(request):
    access_token = request.session.get("access_token", None)
    if access_token == None:  # 로그인 안돼있으면
        return redirect("/kakaologin")  # 무지성 로그아웃 누른애는 로그인하도록 로그인창으로 보내기

    else:
        del request.session['access_token']
        return render(request, 'loginoutsuccess.html')

@csrf_exempt
def good(request):

    return render(request, "good.html")

@csrf_exempt
def go(request):

    return render(request, "go.html")


@csrf_exempt
def alonechoose(request):

    return render(request, "alonechoose.html")
@csrf_exempt
def alonechoose2(request):

    return render(request, "alonechoose2.html")
@csrf_exempt
def army(request):

    return render(request, "army.html")
@csrf_exempt
def body(request):

    return render(request, "body.html")
@csrf_exempt
def eyes(request):

    return render(request, "eyes.html")
@csrf_exempt
def height(request):

    return render(request, "height.html")
@csrf_exempt
def hobby(request):

    return render(request, "hobby.html")

@csrf_exempt
def meeting(request):
    access_token = request.session.get("access_token", None)
    if access_token:
        logged = 1
        account_info = requests.get("https://kapi.kakao.com/v2/user/me",
                                    headers={"Authorization": f"Bearer {access_token}"}).json()
        kakao_id = account_info.get("id")
    if request.method == "POST":
        try:
            # kakao_id=0인 하나의 Info 객체를 가져옴
            user_info = Info.objects.get(kakao_id=kakao_id)
        except Info.DoesNotExist:
            return render(request, "error.html", {"message": "User not found"})

        # 인원 선택 정보 추출
        peoplenum = request.POST.get('submit_peoplenum')  # 단일 값으로 가져옴
        avgage = request.POST.get('submit_age')

        # 값 저장
        user_info.peoplenum = peoplenum
        user_info.avgage = avgage
        user_info.save()

        return redirect("/meeting2")  # /meeting2로 리다이렉트

    return render(request, "meeting.html")


@csrf_exempt
def meeting2(request):
    access_token = request.session.get("access_token", None)
    if access_token:
        logged = 1
        account_info = requests.get("https://kapi.kakao.com/v2/user/me",
                                    headers={"Authorization": f"Bearer {access_token}"}).json()
        kakao_id = account_info.get("id")
    if request.method == "POST":
        try:
            # kakao_id=0인 하나의 Info 객체를 가져옴
            user_info = Info.objects.get(kakao_id=kakao_id)
        except Info.DoesNotExist:
            return render(request, "error.html", {"message": "User not found"})

        # 'submit_job'과 'submit_age' 필드를 처리
        jobs = request.POST.getlist('submit_job')  # 복수 선택 가능 (리스트로 받음)
        age_ranges = request.POST.getlist('submit_age')  # 복수 선택 가능 (리스트로 받음)

        # jobs와 age_ranges 리스트를 문자열로 변환 후 저장
        user_info.jobs = ', '.join(jobs)
        user_info.ages = ', '.join(age_ranges)
        user_info.save()

        return redirect("/good/")  # 성공적으로 처리되면 /good/으로 리다이렉트

    return render(request, "meeting2.html")


@csrf_exempt
def major(request):
    return render(request, "major.html")


@csrf_exempt
def mbti(request):
    return render(request, "mbti.html")


@csrf_exempt
def myinfo(request):
    access_token = request.session.get("access_token", None)
    if access_token == None:  # 로그인 안돼있으면
        return render(request, "kakaologin.html")  # 로그인 시키기

    account_info = requests.get("https://kapi.kakao.com/v2/user/me",
                                headers={"Authorization": f"Bearer {access_token}"}).json()
    kakao_id = account_info.get("id")

    user_profile = Info.objects.get(kakao_id=kakao_id)  # user_info로 바꿀까?
    context = {'user_profile': user_profile,  # 사용자 정보를 context에 추가
               }
    return render(request, "myinfo.html", context)

def is_valid_transition(current_page, requested_page):
    # 요청한 페이지가 현재 페이지에서의 올바른 다음 페이지인지 확인
    requested_page_int = int(requested_page)
    if requested_page_int == current_page + 1 or current_page == requested_page_int :
        return True
    return False

@csrf_exempt
def my(request, id):
    access_token = request.session.get("access_token", None)
    if access_token:
        logged = 1
        account_info = requests.get("https://kapi.kakao.com/v2/user/me",
                                    headers={"Authorization": f"Bearer {access_token}"}).json()

    kakao_id = account_info.get("id")
    if request.method == "GET":
        if int(id) == 1:
            if request.session.get('current_page'):
                del request.session['current_page']

        current_page = request.session.get('current_page', 0)
        if int(id) < current_page:
            current_page = int(id)

        if not is_valid_transition(current_page, id):
            # 올바른 페이지 이동이 아니면 거부
            if current_page == 2 and int(id) == 4 and request.session['sex'] == 'female':  # 여자면 4로 이동되도록 함. 3이 army여야함
                request.session['current_page'] = int(id) - 1
                return redirect("/my/4")
            return HttpResponseForbidden("Forbidden")

        # 페이지 이동을 허용하고, 세션 업데이트
        request.session['current_page'] = int(id)

    # 자기소개 한거 있으면 자기소개 내용 불러오고 choose페이지로 넘어가게

    index = int(id)

    if request.method == "POST":
        if index == 1:
            request.session['age'] = request.POST.get("age")
        elif index == 2:
            request.session['sex'] = request.POST.get("sex")
            if request.session['sex'] == 'female':
                # request.session['army'] = 'female' 이런식으로 여자면 army값을 넣어줘야함 안그러면 아래에서 NULL입력돼서 매칭 안됨
                index += 1
        elif index == 3:
            request.session['army'] = request.POST.get("army")
        elif index == 4:
            request.session['job'] = request.POST.get("job")
        elif index == 5:
            request.session['school'] = request.POST.get("school")
            request.session['major'] = request.POST.get("major")
        elif index == 6:#html에서 id값이 다르면 디비에서 다른 레코드로 되어서 반복문으로 한 글자씩 받아서 추가
            selected_mbti = []
            for i in range(1, 5):
                mbti_value = request.POST.get(f"mbti{i}")
                if mbti_value:
                    selected_mbti.append(mbti_value)
            selected_mbti_str = ''.join(selected_mbti)
            request.session['mbti'] = selected_mbti_str
        elif index == 7:
            request.session['height'] = request.POST.get("height")
        elif index == 8:
            request.session['body'] = request.POST.get("body")
        elif index == 9:
            request.session['eyes'] = request.POST.get("eyes")
        elif index == 10:
            request.session['face'] = request.POST.get("face")
        elif index == 11:
            # hobby 필드는 복수 선택 가능이므로 리스트로 저장
            hobby_list = request.POST.getlist("hobby")
            hobby_str = ', '.join(hobby_list)  # 선택한 취미를 문자열로 합치기
            request.session['hobby'] = hobby_str  # 세션에 저장
        elif index == 12:
            request.session['free'] = request.POST.get("free")
        else:
            index = 1

        index2 = index + 1
        if index2 > 12:  # 모든 정보를 입력한 경우
            # 세션에 저장된 정보를 하나의 Info 객체에 저장하고 세션 초기화
            user_info = Info.objects.get(kakao_id=kakao_id)
            if user_info:
                user_info.age = request.session.get('age')
                user_info.sex = request.session.get('sex')
                user_info.job = request.session.get('job')
                user_info.school = request.session.get('school')
                user_info.major = request.session.get('major')
                user_info.mbti = request.session.get('mbti')
                user_info.army = request.session.get('army')
                user_info.height = request.session.get('height')
                user_info.body = request.session.get('body')
                user_info.eyes = request.session.get('eyes')
                user_info.face = request.session.get('face')
                user_info.hobby = request.session.get('hobby')
                user_info.free = request.session.get('free')
                user_info.save()
            else:#이미 로그인 한 상태라 레코드 새로 생성하는 예외처리는 없어도 될 듯
                myinfo = Info.objects.create(
                    kakao_id=kakao_id,
                    age=request.session.get('age'),
                    sex=request.session.get('sex'),
                    job=request.session.get('job'),
                    school=request.session.get('school'),
                    major=request.session.get('major'),
                    mbti=request.session.get('mbti'),
                    army=request.session.get('army'),
                    height=request.session.get('height'),
                    body=request.session.get('body'),
                    eyes=request.session.get('body'),
                    face=request.session.get('face'),
                    hobby=request.session.get('hobby'),
                    free=request.session.get('free')
                )
            return redirect("/kakaoid/")  # 모든 정보를 입력한 후 성공 페이지로 이동
        else:
            return redirect(f"/my/{index2}")  # 다음 페이지로 이동

    context = {'count': index}
    return render(request, "my.html", context)

@csrf_exempt
def you(request):

    return render(request, "you.html")

@csrf_exempt
def choose(request):
    #홍대축제에서 만나기 누르면 choose에서는 무조건 meeting으로 redirect
    return render(request, "choose.html")

@csrf_exempt
def success(request):
        return render(request, "success.html")

@csrf_exempt
def fail(request):

    return render(request, "fail.html")

@csrf_exempt
def youinfo(request):
    access_token = request.session.get("access_token", None)
    if access_token == None:  # 로그인 안돼있으면
        return render(request, "kakaologin.html")  # 로그인 시키기

    account_info = requests.get("https://kapi.kakao.com/v2/user/me",
                                headers={"Authorization": f"Bearer {access_token}"}).json()
    kakao_id = account_info.get("id")

    user_profile = Info.objects.get(kakao_id=kakao_id)  # user_info로 바꿀까?
    matches = find_matches(user_profile)

    if matches.exists():
        # 첫 번째 매칭 상대 가져오기
        first_match = matches.first()
        context = {'matched_profile': first_match,  # 사용자 정보를 context에 추가
                   }

    return render(request, "youinfo.html", context)

def kakao(request):
    access_token = request.session.get("access_token", None)
    if access_token == None:  # 로그인 안돼있으면
        return render(request, "myapp/kakaologin.html")  # 로그인 시키기

    account_info = requests.get("https://kapi.kakao.com/v2/user/me",
                                headers={"Authorization": f"Bearer {access_token}"}).json()
    kakao_id = account_info.get("id")

    user_profile = Info.objects.get(kakao_id=kakao_id)  # user_info로 바꿀까?
    matches = find_matches(user_profile)

    if matches.exists():
        # 첫 번째 매칭 상대 가져오기
        first_match = matches.first()
        context = {'matched_profile': first_match,  # 사용자 정보를 context에 추가
                   }

    return render(request, "kakao.html", context)


@csrf_exempt
def kakaoid(request):
    access_token = request.session.get("access_token",None)
    if access_token == None: #로그인 안돼있으면
        return redirect("/kakaologin")

    account_info = requests.get("https://kapi.kakao.com/v2/user/me",headers={"Authorization": f"Bearer {access_token}"}).json()

    if request.method == "POST":
        kakao_id = account_info.get("id")

        # kakao_id를 사용하여 해당 사용자의 레코드 가져오기
        user_info = Info.objects.get(kakao_id=kakao_id)

        kakaotalk_id = request.POST.get("kakaoid")
        if kakaotalk_id is not None:
            # 가져온 레코드에 kakaotalk_id 할당 및 저장
            user_info.kakaotalk_id = kakaotalk_id
            user_info.save()
            return redirect("/go")

    return render(request, "kakaoid.html")

def calculate_match_score(user, potential_match):
    score = 0

    if potential_match.age:
        age_diff = abs(user.age - potential_match.age)
        score += max(0, 10 - age_diff)

    if user.job and potential_match.job and user.job == potential_match.job:
        score += 5

    if user.mbti and potential_match.mbti and user.mbti == potential_match.mbti:
        score += 10

    if user.height and potential_match.height:
        height_diff = abs(user.height - potential_match.height)
        score += max(0, 5 - (height_diff // 5))

    if user.hobby and potential_match.hobby:
        user_hobbies = set(user.hobby.split(', '))
        match_hobbies = set(potential_match.hobby.split(', '))
        common_hobbies = len(user_hobbies & match_hobbies)
        score += common_hobbies * 2

    return score

def find_matches(user_info):
    opposite_sex = 'male' if user_info.sex == 'female' else 'female'

    individual_matches = Info.objects.filter(
        Q(sex=opposite_sex),
        Q(age__range=(int(user_info.age) - 2, int(user_info.age) + 2)),  # 나이차 2살 허용
        Q(job=user_info.job) | Q(hobby__icontains=user_info.hobby)  # 직업 또는 취미가 하나라도 겹치면 매칭
    )

    matching_teams = Info.objects.filter(
        Q(peoplenum=user_info.peoplenum),  # 인원 수가 동일한 경우
        Q(avgage__range=(int(user_info.avgage) - 5, int(user_info.avgage) + 5)),  # 평균 나이대 5살 차이 허용
        Q(jobs__icontains=user_info.jobs),  # 직업이 하나라도 일치하는지 확인
        Q(ages__icontains=user_info.ages)   # 나이대가 하나라도 일치하는지 확인
    )

    return matching_teams.distinct()


def find_matches(user_info):
    # 자신의 성별에 따라 반대 성별을 찾도록 설정
    opposite_sex = 'male' if user_info.sex == 'female' else 'female'

    # peoplenum 필터링 (무조건 하나라도 일치해야 함)
    peoplenum_filter = Q()
    user_peoplenum_list = [int(num) for num in user_info.peoplenum.split(',')]  # peoplenum 리스트로 변환

    for num in user_peoplenum_list:
        peoplenum_filter |= Q(peoplenum__contains=str(num))

    # 1. sex와 peoplenum이 일치하는 프로필 필터링
    matching_profiles = Info.objects.filter(
        peoplenum_filter,
        sex=opposite_sex  # 반대 성별 필터 적용
    )

    # 2. age와 job 조건 필터링
    ages_filter = Q()
    for age_range in user_info.ages.split(','):
        start_age, end_age = map(int, age_range.split('-'))
        ages_filter |= Q(avgage__range=(start_age, end_age))

    jobs = user_info.jobs.split(',')  # jobs도 리스트로 변환

    # 첫 번째 우선순위: 나이와 직업이 모두 일치하는 상대
    both_values_matches = matching_profiles.filter(
        ages_filter,
        job__in=jobs
    )
    print("Matches after both age and job filtering:", both_values_matches)

    if both_values_matches.exists():
        # 나이와 직업이 모두 일치하는 상대가 있으면 그 결과를 반환
        return both_values_matches.distinct()
    else:
        # 두 번째 우선순위: 나이 또는 직업 중 하나만 일치하는 상대
        either_values_matches = matching_profiles.filter(
            ages_filter | Q(job__in=jobs)
        )
        print("Matches after either age or job filtering:", either_values_matches)

        if either_values_matches.exists():
            # 나이 또는 직업 중 하나만 일치하는 상대가 있으면 그 결과를 반환
            return either_values_matches.distinct()

        # 매칭되는 결과가 없을 경우 모든 프로필 중에서 성별만 반대인 첫 번째 프로필 반환
        fallback_match = Info.objects.filter(sex=opposite_sex).first()
        if fallback_match:
            return [fallback_match]  # 단일 객체를 리스트로 반환

    # 매칭되는 결과가 없을 경우 빈 쿼리셋 반환
    return Info.objects.none()

def save_first_match(user_info):
    matches = find_matches(user_info)

    if matches.exists():
        # 첫 번째 매칭 상대 가져오기
        first_match = matches.first()

        # matchingInfo에 매칭 정보 저장
        matching = matchingInfo.objects.create(
            matchingnum=generate_matching_number(),  # matchingnum은 고유번호 생성 함수
            matched=first_match  # 성별에 관계없이 matched 컬럼에 저장
        )
        matching.save()

        return matching

    else:
        # 매칭 상대가 없을 경우 None 반환
        return None


def generate_matching_number():
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def find_and_render_match(request):
    # 현재 로그인된 사용자 정보를 가져옴
    user_info = Info.objects.get(kakao_id=request.session.get("user_profile"))

    # 첫 번째 매칭 결과를 찾음
    match = save_first_match(user_info)


    # 매칭된 상대가 있으면 결과를 렌더링
    if match:
        context = {
            'matched': match.matched,
            'peoplenum': user_info.peoplenum,
        }
    else:
        context = {
            'error': '매칭된 상대가 없습니다.'
        }

    # result.html로 데이터 전달
    return render(request, 'result.html', context)