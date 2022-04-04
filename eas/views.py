from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render

from django.http import  HttpResponse

def index(request):
    template = loader.get_template('eas/index.html')
    return render(request, 'eas/index.html')

def detail(request):
    question = get_object_or_404
    return render(request, 'eas/detail.html')