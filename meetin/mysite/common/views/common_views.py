import requests
from django.shortcuts import render, redirect


def home(request):

    return render(request, "myapp/home.html")

@csrf_exempt
def menu(request):

    return render(request,"myapp/menu.html")


def kakaologin(request):
    # context = {'check':False} 지운다?
    access_token = request.session.get("access_token", None)
    if access_token:  # 만약 세션에 access_token이 있으면(==로그인 되어 있으면)


        return redirect("/home")  # 로그인 되어있으면 home페이지로 #로그인 되어있으면 home페이지로

    return render(request, "myapp/kakaologin.html")  # 로그인 안되어있으면 로그인페이지로


def kakaoLoginLogic(request):

    return redirect(_url)


def kakaoLoginLogicRedirect(request):


    return redirect("/home")  # 로그인 완료 후엔 home페이지로

@csrf_exempt
def good(request):

    return render(request, "myapp/good.html")

@csrf_exempt
def go(request):

    return render(request, "myapp/go.html")


@csrf_exempt
def alonechoose(request):

    return render(request, "myapp/alonechoose.html")
@csrf_exempt
def alonechoose2(request):

    return render(request, "myapp/alonechoose2.html")
@csrf_exempt
def army(request):

    return render(request, "myapp/army.html")
@csrf_exempt
def body(request):

    return render(request, "myapp/body.html")
@csrf_exempt
def eyes(request):

    return render(request, "myapp/eyes.html")
@csrf_exempt
def height(request):

    return render(request, "myapp/height.html")
@csrf_exempt
def hobby(request):

    return render(request, "myapp/hobby.html")