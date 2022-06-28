from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    # return redirect('https://picsum.photos/1080/620/?random')
    return redirect('http://3.37.211.248/eos')