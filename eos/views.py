from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request,"https://picsum.photos/1080/620/?random")