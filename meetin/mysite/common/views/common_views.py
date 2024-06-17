import requests
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
   return redirect("/home")

def home(request):

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
        peoplenum = request.POST.get('submit_peoplenum') #인원 선택 정보 추출
        avgage = request.POST.get('submit_age')
        return redirect("/meeting2")  # /home/meeting2로 페이지 전달

    return render(request, "myapp/meeting.html")


@csrf_exempt
def meeting2(request):
    if request.method == "POST":
        jobs = request.POST.get('submit_job').split(', ')
        ages = request.POST.get('submit_age').split(', ')
        return redirect("/good/")

    return render(request, "myapp/meeting2.html")