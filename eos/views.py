from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    HttpResponse('eos/index.html')