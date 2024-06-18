import requests
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from ..models import Info


@csrf_exempt
def index(request):
   return redirect("/home")

def home(request):
    user_info = Info.objects.filter(kakao_id=0)

    return render(request, "home.html")

@csrf_exempt
def menu(request):

    return render(request,"menu.html")


def kakaologin(request):
    # context = {'check':False} 지운다?
    access_token = request.session.get("access_token", None)
    if access_token:  # 만약 세션에 access_token이 있으면(==로그인 되어 있으면)


        return redirect("/home")  # 로그인 되어있으면 home페이지로 #로그인 되어있으면 home페이지로

    return render(request, "kakaologin.html")  # 로그인 안되어있으면 로그인페이지로


def kakaoLoginLogic(request):

    return redirect(_url)


def kakaoLoginLogicRedirect(request):


    return redirect("/home")  # 로그인 완료 후엔 home페이지로

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
        user_info = Info.objects.filter(kakao_id=0)
        peoplenum = request.POST.get('submit_peoplenum') #인원 선택 정보 추출
        avgage = request.POST.get('submit_age')
        return redirect("/meeting2")  # /home/meeting2로 페이지 전달

    return render(request, "myapp/meeting.html")


@csrf_exempt
def meeting2(request):
    if request.method == "POST":
        user_info = Info.objects.filter(kakao_id=0)
        jobs = request.POST.get('submit_job').split(', ')
        ages = request.POST.get('submit_age').split(', ')
        return redirect("/good/")

    return render(request, "myapp/meeting2.html")


@csrf_exempt
def major(request):
    return render(request, "myapp/major.html")


@csrf_exempt
def mbti(request):
    return render(request, "myapp/mbti.html")


@csrf_exempt
def myinfo(request):
    user_info = Info.objects.filter(kakao_id=0)
    return render(request, "myapp/myinfo.html")

def is_valid_transition(current_page, requested_page):
    # 요청한 페이지가 현재 페이지에서의 올바른 다음 페이지인지 확인
    requested_page_int = int(requested_page)
    if requested_page_int == current_page + 1 or current_page == requested_page_int :
        return True
    return False

@csrf_exempt
def my(request, id):
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