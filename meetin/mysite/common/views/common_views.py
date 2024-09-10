import requests
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from ..models import Info


@csrf_exempt
def index(request):
   return redirect("/home")


@csrf_exempt
def home(request):
    logged = 0

    access_token = request.session.get("access_token", None)
    if access_token:
        logged = 1
        account_info = requests.get("https://kapi.kakao.com/v2/user/me",
                                    headers={"Authorization": f"Bearer {access_token}"}).json()
        kakao_id = account_info.get("id")
        user_info = Info.objects.filter(kakao_id=kakao_id).first()
    context = {'logged': logged}
    return render(request, "home.html", context)

@csrf_exempt
def menu(request):

    return render(request,"menu.html")


def kakaologin(request):
    # context = {'check':False} 지운다?
    access_token = request.session.get("access_token", None)
    if access_token:  # 만약 세션에 access_token이 있으면(==로그인 되어 있으면)
        account_info = requests.get("https://kapi.kakao.com/v2/user/me",
                                    headers={"Authorization": f"Bearer {access_token}"}).json()
        kakao_id = account_info.get("id")
        try:  # 어차피 access_token이 있어야 하니까 예외 처리는 없어도 될 듯
            user_profile = Info.objects.get(kakao_id=kakao_id)  # 카카오톡 ID를 사용하여 사용자 정보 조회
            # print(kakao_id) 지운다?
            # context['user_profile'] = user_profile 지운다?
        except Info.DoesNotExist:
            # 새로운 레코드 생성
            user_profile = Info(kakao_id=kakao_id)
            user_profile.save()
            # context['user_profile'] = user_profile 지운다?

        return redirect("/home")  # 로그인 되어있으면 home페이지로 #로그인 되어있으면 home페이지로

    return render(request, "kakaologin.html")  # 로그인 안되어있으면 로그인페이지로


def kakaoLoginLogic(request):
    _restApiKey = 'bf24f04aa4c3aabf2644d871e7673f65'  # 입력필요
    _redirectUrl = 'http://ec2-52-79-77-37.ap-northeast-2.compute.amazonaws.com:8080/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)


def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = 'bf24f04aa4c3aabf2644d871e7673f65'  # 입력필요
    _redirect_uri = 'http://ec2-52-79-77-37.ap-northeast-2.compute.amazonaws.com:8080/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True

    return redirect("/home")  # 로그인 완료 후엔 home페이지로


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
    if request.method == "POST":
        try:
            # kakao_id=0인 하나의 Info 객체를 가져옴
            user_info = Info.objects.get(kakao_id=0)
        except Info.DoesNotExist:
            # Info 객체가 없을 경우 예외 처리
            return render(request, "error.html", {"message": "User not found"})

        # 인원 선택 정보 추출
        peoplenum = request.POST.getlist('submit_peoplenum')  # 'getlist()'로 리스트 형태로 가져옴
        avgage = request.POST.get('submit_age')

        # peoplenum 리스트를 문자열로 합침
        user_info.peoplenum = ', '.join(peoplenum)
        user_info.avgage = avgage
        user_info.save()

        return redirect("/meeting2")  # /meeting2로 리다이렉트

    return render(request, "meeting.html")


@csrf_exempt
def meeting2(request):
    if request.method == "POST":
        try:
            # kakao_id=0인 하나의 Info 객체를 가져옴
            user_info = Info.objects.get(kakao_id=0)
        except Info.DoesNotExist:
            # Info 객체가 없을 경우 예외 처리
            return render(request, "error.html", {"message": "User not found"})

        # 'submit_job'과 'submit_age' 필드를 처리
        jobs = request.POST.get('submit_job', '').split(', ')
        ages = request.POST.get('submit_age', '').split(', ')

        # jobs와 ages 리스트를 문자열로 변환 후 저장
        user_info.jobs = ', '.join(jobs)
        user_info.ages = ', '.join(ages)
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
        return render(request, "myapp/kakaologin.html")  # 로그인 시키기

    account_info = requests.get("https://kapi.kakao.com/v2/user/me",
                                headers={"Authorization": f"Bearer {access_token}"}).json()
    kakao_id = account_info.get("id")

    user_profile = Info.objects.get(kakao_id=0)  # user_info로 바꿀까?
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
            user_info = Info.objects.get(kakao_id=0)
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

    return render(request, "youinfo.html")

@csrf_exempt
def kakaoid(request):
    access_token = request.session.get("access_token",None)
    if access_token == None: #로그인 안돼있으면
        return redirect("/kakaologin")

    account_info = requests.get("https://kapi.kakao.com/v2/user/me",headers={"Authorization": f"Bearer {access_token}"}).json()

    if request.method == "POST":
        kakao_id = account_info.get("id")

        # kakao_id를 사용하여 해당 사용자의 레코드 가져오기
        user_info = Info.objects.get(kakao_id=0)

        kakaotalk_id = request.POST.get("kakaoid")
        if kakaotalk_id is not None:
            # 가져온 레코드에 kakaotalk_id 할당 및 저장
            user_info.kakaotalk_id = kakaotalk_id
            user_info.save()
            return redirect("/go")

    return render(request, "kakaoid.html")