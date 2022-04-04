from django.shortcuts import render
from django.template import loader

from django.http import  HttpResponse

def index(request):
    template = loader.get_template('eas/index.html')
    return render(request, 'eas/index.html')
