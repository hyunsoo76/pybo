from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect
# from django.template import loader
from django.shortcuts import get_object_or_404, render

from . import pushmsg
from .models import Request
from .forms import RequestForm
from django.core.paginator import Paginator
from django.db.models import Q
from asgiref.sync import sync_to_async



def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    Request_list = Request.objects.order_by('-create_date')
    if kw:
        Request_list = Request_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(a_1__icontains=kw) |  # 매입처명
            Q(b_1__icontains=kw) |
            Q(c_1__icontains=kw) |
            Q(d_1__icontains=kw) |
            Q(e_1__icontains=kw) |
            Q(f_1__icontains=kw) |
            Q(g_1__icontains=kw) |
            Q(h_1__icontains=kw) |
            Q(i_1__icontains=kw) |
            Q(j_1__icontains=kw) |
            Q(a_4__icontains=kw) |  # 계좌명
            Q(b_4__icontains=kw) |
            Q(d_4__icontains=kw) |
            Q(e_4__icontains=kw) |
            Q(f_4__icontains=kw) |
            Q(g_4__icontains=kw) |
            Q(h_4__icontains=kw) |
            Q(i_4__icontains=kw) |
            Q(j_4__icontains=kw) |
            Q(a_5__icontains=kw) |  # 금액
            Q(b_5__icontains=kw) |
            Q(c_5__icontains=kw) |
            Q(d_5__icontains=kw) |
            Q(e_5__icontains=kw) |
            Q(f_5__icontains=kw) |
            Q(g_5__icontains=kw) |
            Q(h_5__icontains=kw) |
            Q(i_5__icontains=kw) |
            Q(j_5__icontains=kw) |
            Q(a_7__icontains=kw) |  # 비고
            Q(b_7__icontains=kw) |
            Q(c_7__icontains=kw) |
            Q(d_7__icontains=kw) |
            Q(e_7__icontains=kw) |
            Q(f_7__icontains=kw) |
            Q(g_7__icontains=kw) |
            Q(h_7__icontains=kw) |
            Q(i_7__icontains=kw) |
            Q(j_7__icontains=kw)
        ).distinct()
    # context = {'Request_list': Request_list}
    paginator = Paginator(Request_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'Request_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'eas/index.html', context)

def detail(request, Request_id):
    new_Request = get_object_or_404(Request, pk=Request_id)
    if new_Request.a_5 > 100:
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
    else:
        new_Request = get_object_or_404(Request, pk=Request_id)
        context = {'new_Request': new_Request}
        return render(request, 'eas/monthly_holiday_r.html', context)







def Request_create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_Request = form.save(commit=False)
            new_Request.create_date = timezone.now()
            new_Request.save()
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

            # return redirect('eas:index')
    else:
        form = RequestForm()
    context = {'form': form}
    return render(request, 'eas/detail.html', context)

# 상신버튼클릭시 push 보내기위해서

def Request_create_sangsin(request, new_Request_id):
    new_Request = get_object_or_404(Request, pk=new_Request_id)
    if request.method == 'POST':
        temp_s = request.POST.get('temp_sangsin')
        if temp_s == "상신":
            from importlib import reload
            reload(pushmsg)
            # await reload(sync_to_async(pushmsg.main()))
            return redirect('eas:index')
    else:
        return redirect('eas:index')


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
            from importlib import reload
            reload(pushmsg)
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
            from importlib import reload
            reload(pushmsg)
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def Request_modify(request, new_Request_id):
    new_Request = get_object_or_404(Request, pk=new_Request_id)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=new_Request)
        if form.is_valid():
            new_Request = form.save(commit=False)
            new_Request.create_date = timezone.now()  # 수정일시 저장

            totals = [new_Request.a_5, new_Request.b_5, new_Request.c_5,
                      new_Request.d_5, new_Request.e_5, new_Request.f_5,
                      new_Request.g_5, new_Request.h_5, new_Request.i_5,
                      new_Request.j_5]
            totalsum = 0
            for total in totals:
                if total != None:
                    totalsum = totalsum + total
            new_Request.total = totalsum

            new_Request.save()
            context = {'new_Request': new_Request}
            return render(request, 'eas/detail_r.html', context)

            # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            # return redirect('eas:index')
    else:
        form = RequestForm(instance=new_Request)
        context = {'form': form}
        return render(request, 'eas/detail_modify.html', context)



def detail_modify(request, Request_id):
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

# 휴가품의 insert
def monthly_holiday(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_Request = form.save(commit=False)
            new_Request.create_date = timezone.now()
            new_Request.save()
            # context = {'new_Request': new_Request}
            # return render(request, 'eas/monthly_holiday_r.html', context)
            return redirect('eas:index')
    else:
        form = RequestForm()
        context = {'form': form}
        return render(request, 'eas/monthly_holiday.html', context)

# 휴가품의 read
def monthly_holiday_r(request, Request_id):
    new_Request = get_object_or_404(Request, pk=Request_id)

    context = {'new_Request': new_Request}
    return render(request, 'eas/monthly_holiday_r.html', context)

# 휴가품의 대표이사결재란 승인
def monthly_holiday_r_okupdate2(request, new_Request_id):
    new_Request = get_object_or_404(Request, pk=new_Request_id)
    if request.method == "POST":
        temp = request.POST.get('input_ok2')
        if new_Request.bbb != "반려":
            new_Request.bbb = temp
            new_Request.aaa = "승인"
            if new_Request.date2 ==None:
                new_Request.date2 = timezone.now()
            new_Request.save()

            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    from importlib import reload
    reload(pushmsg)


# 휴가품의 대표결재란 번려
def monthly_holiday_r_update2(request, new_Request_id):
    new_Request = get_object_or_404(Request, pk=new_Request_id)
    if request.method == "POST":
        temp = request.POST.get('input_reject2')
        if new_Request.bbb != "승인":
            new_Request.bbb = temp
            new_Request.aaa = "승인"
            new_Request.date2 = timezone.now()
            new_Request.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

