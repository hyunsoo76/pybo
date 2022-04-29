from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Request
from .forms import RequestForm
from django.http import  HttpResponse
from django.core.paginator import Paginator


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    Request_list = Request.objects.order_by('-create_date')
    # context = {'Request_list': Request_list}
    paginator = Paginator(Request_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'Request_list': page_obj}
    return render(request, 'eas/index.html', context)

def detail(request, Request_id):
    new_Request = get_object_or_404(Request, pk=Request_id)
    totals = [new_Request.a_5, new_Request.b_5, new_Request.c_5,
              new_Request.d_5, new_Request.e_5, new_Request.f_5,
              new_Request.g_5, new_Request.h_5, new_Request.i_5,
              new_Request.j_5]
    totalsum = 0
    for total in totals:
        if total != None:
            totalsum = totalsum + total

    new_Request.total = totalsum

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

def detail_update(request, new_Request_id):
    new_Request = get_object_or_404(Request, pk=new_Request_id)
    if request.method == "POST":
        temp = request.POST.get('input_reject')
        if new_Request.aaa != "승인":
            new_Request.aaa = temp
            new_Request.date1 = timezone.now()
            new_Request.save()
            messages.warning(request, "결재완료")
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))



def detail_okupdate(request, new_Request_id):
    new_Request = get_object_or_404(Request, pk=new_Request_id)
    if request.method == "POST":
        temp = request.POST.get('input_ok')
        if new_Request.aaa != "반려":
            new_Request.aaa = temp
            new_Request.date1 = timezone.now()
            new_Request.save()
            messages.warning(request, "결재완료")
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def detail_update2(request, new_Request_id):
    new_Request = get_object_or_404(Request, pk=new_Request_id)
    if request.method == "POST":
        temp = request.POST.get('input_reject2')
        if new_Request.bbb != "승인":
            new_Request.bbb = temp
            new_Request.date2 = timezone.now()
            new_Request.save()
            messages.warning(request, "결재완료")
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def detail_okupdate2(request, new_Request_id):
    new_Request = get_object_or_404(Request, pk=new_Request_id)
    if request.method == "POST":
        temp = request.POST.get('input_ok2')
        if new_Request.bbb != "반려":
            new_Request.bbb = temp
            new_Request.date2 = timezone.now()
            new_Request.save()
            messages.warning(request, "결재완료")
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
