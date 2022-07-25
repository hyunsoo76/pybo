from django.core.paginator import Paginator
# from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q
from .forms import Order_listForm
from .models import Products
from .models import Order_list
import csv
import pandas as pd
from django.contrib import messages


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    Order_lists = Order_list.objects.order_by('-od_date')
    if kw:
        Order_lists = Order_lists.filter(
            Q(buyer_name__icontains=kw) |  #
            # Q(d_day__icontains=kw) |  #
            # Q(od_date__icontains=kw) |
            Q(p_name__icontains=kw)
            # Q(sale_bar__icontains=kw) |
            # Q(org_bar__icontains=kw)
        ).distinct()
    # context = {'Order_lists': Order_lists}
    paginator = Paginator(Order_lists, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'Order_lists': page_obj, 'page': page, 'kw': kw}
    return render(request, 'eos/index.html', context)


# def order_page(request):
#     return render(request, 'eos/order_page.html')

class ProductView(ListView):
    model = Products
    template_name = 'eos/product.html'


# 상품db 업데이트
def p_list(request):
    with open("/home/ubuntu/projects/mysite/static/p_list.csv", "r", encoding='cp949') as f:
        dr = csv.DictReader(f)
        s = pd.DataFrame(dr)
    ss = []
    for i in range(len(s)):
        # st = (s["ID"][i], s["상품명"][i], s["바코드"][i], s["입수"][i], s["납품가"][i], s["원코드"][i], s["위치정보"][i])
        Products.objects.create(p_id=s["ID"][i],
                                p_name=s["상품명"][i],
                                sale_bar=s["바코드"][i],
                                iq=s["입수"][i],
                                p_price=s["납품가"][i],
                                org_bar=s["원코드"][i],
                                location=s["위치정보"][i])


# 발주등록 order_page
# def order_create(request):
#     if request.method == 'POST':
#         form = Order_listForm(request.POST)
#         if form.is_valid():
#             new_order_list = form.save(commit=False)
#             new_order_list.od_date = timezone.now()
#             input_cal = request.POST.get('calender')
#             input_buyer = request.POST.get('buyer_select')
#             new_order_list.d_day = input_cal
#             new_order_list.buyer_name = input_buyer
#             barcode = request.POST.get('barcode_input')
#             if (new_order_list.buyer_name == '발주 매장 선택') or (type(barcode) == str) or (new_order_list.d_day == ""):
#                 new_order_list = form.save(commit=False)
#                 context = {'new_order_list': new_order_list}
#                 return render(request, 'eos/order_page.html', context)
#             else:
#                 occonunt = request.POST.get('od_count_input')
#                 odbox = request.POST.get('od_box_count_input')
#                 if odbox != '':  # 낱개발주 와 박스 발주 동시입력시 낱개 발주 0처리
#                    new_order_list.fff = barcode
#                    new_order_list.od_count = 0
#                    new_order_list.od_box_count = odbox
#                    new_order_list.save()
#                    context = {'new_order_list': new_order_list}
#                    return render(request, 'eos/order_page_r.html', context)
#                 else :
#                    new_order_list.fff = barcode
#                    new_order_list.od_count = occonunt
#                    new_order_list.save()
#                    context = {'new_order_list': new_order_list}
#                    return render(request, 'eos/order_page_r.html', context)
#         else:
#             form = Order_listForm(request.POST)
#             context = {'form': form}
#             return render(request, 'eos/order_page.html', context)
#     else:
#         form = Order_listForm()
#         context = {'form': form}
#         return render(request, 'eos/order_page.html', context)

def order_page(request, Order_list_id):
    new_order_list = get_object_or_404(Order_list, pk=Order_list_id)
    context = {'new_order_list': new_order_list}
    return render(request, 'eos/order_page_r.html', context)


def order_create(request):
    if request.method == 'POST':
        form = Order_listForm(request.POST)
        if form.is_valid():
            new_order_list = form.save(commit=False)
            new_order_list.od_date = timezone.now()
            input_cal = request.POST.get('calender')
            input_buyer = request.POST.get('buyer_select')
            new_order_list.d_day = input_cal
            new_order_list.buyer_name = input_buyer
            barcode = request.POST.get('barcode_input')
            occonunt = request.POST.get('od_count_input')
            odbox = request.POST.get('od_box_count_input')
            # new_order_list.od_box_count = odbox
            # new_order_list.od_count = occonunt
            new_order_list.fff = barcode
            # new_order_list.save()

            # 매장명 미 입력시 오류메시지 표시- 표시는되나 입력값 초기화 되는 문제 미해결
            # if new_order_list.buyer_name == '':
            #     # some_function(request)
            #     messages.error(request, "발주매장 선택하세요")
            #     form = Order_listForm(request.POST)
            #     context = {'form': form}
            #     return render(request, 'eos/order_page.html', context)
            # else:
            #     pass

            if odbox != '':  # 낱개발주 와 박스 발주 동시입력시 낱개 발주 0처리
                # new_order_list.fff = barcode
                new_order_list.od_count = 0
                new_order_list.od_box_count = odbox
                new_order_list.save()
                context = {'new_order_list': new_order_list}
                return render(request, 'eos/order_page_r.html', context)
            else:
                # new_order_list.fff = barcode
                new_order_list.od_count = occonunt
                new_order_list.od_box_count = 0
                new_order_list.save()
                context = {'new_order_list': new_order_list}
                return render(request, 'eos/order_page_r.html', context)

            # new_order_list.save()
            # context = {'new_order_list': new_order_list}
            # return render(request, 'eos/order_page_r.html', context)



        else:
            # form = Order_listForm(request.POST)
            context = {'form': form}
            return render(request, 'eos/order_page.html', context)
    else:
        form = Order_listForm()
        context = {'form': form}
        return render(request, 'eos/order_page.html', context)


def some_function(request):
    messages.error(request, "발주매장 선택하세요")
    # order_create(request)
# 메시지 팝업
# def some_function(request):
#     messages.warning(request, "낱개발주와 박스발주 같이 입력하면 낱개발주 0 으로 됨.")
