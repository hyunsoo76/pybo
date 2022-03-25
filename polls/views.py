from django.shortcuts import render
from django.http import HttpResponse


def index1(request):
    return render(request, 'polls/main.html')
