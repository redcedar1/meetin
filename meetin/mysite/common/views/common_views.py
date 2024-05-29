import requests
from django.shortcuts import render


def home(request):

    return render(request, "myapp/home.html")

@csrf_exempt
def menu(request):

    return render(request,"myapp/menu.html")