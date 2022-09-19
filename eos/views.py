from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.db.models import Q
from .forms import Order_listForm
from .models import Products
from .models import Order_list
from django.core.exceptions import ObjectDoesNotExist
import csv
import pandas as pd
from django.contrib import messages
import json
from django.http import JsonResponse
from cart.models import Cart, CartItem


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



def order_page(request, Order_list_id):
    new_order_list = get_object_or_404(Order_list, pk=Order_list_id)
    context = {'new_order_list': new_order_list}
    return render(request, 'eos/order_page_r.html', context)



# 기존 order_create--------------------------------
def order_create(request):
    if request.method == 'POST':
        form = Order_listForm(request.POST)
        if form.is_valid():
            new_order_list = form.save(commit=False)
            new_order_list.od_date = timezone.now()
            input_cal = request.POST.get('calender')
            new_order_list.d_day = input_cal
            input_buyer = request.POST.get('buyer_select')
            new_order_list.buyer_name = input_buyer
            # jsonfield save
            data = request.POST.getlist('input[]')
            new_order_list.od_list = data

            # Product Class 조회 변수 저장
            psb = Products.objects.get(sale_bar=(new_order_list.od_list[0]))
            new_order_list.s_product = psb.p_name
            new_order_list.s_iq = psb.iq
            new_order_list.s_price = psb.p_price
            new_order_list.s_location = psb.location
            new_order_list.s_org_bar = psb.org_bar
            new_order_list.save()

            context = {'new_order_list': new_order_list}
            return render(request, 'eos/order_page_r.html', context)
        else:
            context = {'form': form}
            return render(request, 'eos/order_page.html', context)
    else:
        form = Order_listForm()
        context = {'form': form}
        return render(request, 'eos/order_page.html', context)
# 기존 order_create--------------------------------






def some_function(request):
    messages.error(request, "발주매장 선택하세요")
    # order_create(request)
# 메시지 팝업
# def some_function(request):
#     messages.warning(request, "낱개발주와 박스발주 같이 입력하면 낱개발주 0 으로 됨.")



@csrf_exempt
def searchData(request):
    # POST 요청일 때
    if 'searchwords' in request.POST:
        data = request.POST['searchwords']
        s_data = Products.objects.get(sale_bar=(data))
        s_p_name = s_data.p_name
        s_p_iq = s_data.iq
        s_p_price = s_data.p_price
        s_p_location = s_data.location
        s_p_org_bar = s_data.org_bar

        context = {
            'result': s_p_name,
            'result_iq': s_p_iq,
            'result_price': s_p_price,
            'result_location': s_p_location,
            'result_org_bar': s_p_org_bar,
        }

        return JsonResponse(context)

