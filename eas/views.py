from django.utils import timezone

from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Request
from .forms import RequestForm
from django.http import  HttpResponse

def index(request):
    Request_list = Request.objects.order_by('-create_date')
    context = {'Request_list': Request_list}
    return render(request, 'eas/index.html', context)

def detail(request, Request_id):
    new_Request = get_object_or_404(Request, pk=Request_id)
    context = {'new_Request': new_Request}

    return render(request, 'eas/detail_r.html', context)

def Request_create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_Request = form.save(commit=False)
            new_Request.create_date = timezone.now()
            new_Request.save()
            return redirect('eas:index')
    else:
        form = RequestForm()
    context = {'form': form}
    return render(request, 'eas/detail.html', context)

def detail_r_dojang(request, new_Rquest_id):

            new_detail = get_object_or_404(Request, pk=new_Rquest_id)
            # new_detail = get_object_or_404(Request, pk=Request_id)
            # new_detail.create_date = timezone.now()
            new_detail.aaa = "반려"
            new_detail.save()
            context = {'new_detail': new_detail}

            return render(request, 'eas/detail_r.html', context)

            return redirect('eas:detail_r')
