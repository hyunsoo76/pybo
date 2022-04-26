from django.utils import timezone

from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Request
from .forms import RequestForm
from django.http import HttpResponse, HttpResponseRedirect


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
            return HttpResponseRedirect(reverse('eas:index'))
    else:
        form = RequestForm()
    context = {'form': form}
    return render(request, 'eas/detail.html', context)

def detail_update(request, new_Request_id):
    new_Request = get_object_or_404(Request, pk=new_Request_id)
    if request.method == "POST":
        temp = request.POST.get('input_reject')
        if new_Request.aaa != "승인":
            new_Request.aaa = temp
            new_Request.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def detail_okupdate(request, new_Request_id):
    new_Request = get_object_or_404(Request, pk=new_Request_id)
    if request.method == "POST":
        temp = request.POST.get('input_ok')
        if new_Request.aaa != "반려":
            new_Request.aaa = temp
            new_Request.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))