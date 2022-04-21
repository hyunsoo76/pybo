from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Request

from django.http import  HttpResponse

def index(request):
    Request_list = Request.objects.order_by('-create_date')
    context = {'Request_list': Request_list}
    return render(request, 'eas/index.html', context)

def detail(request, Request_id):
    Request = Request.objects.get(id=Request_id)
    context = {'Request': Request}
    return render(request, 'eas/detail.html', context)