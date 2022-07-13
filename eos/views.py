from django.core.paginator import Paginator
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q
from .forms import Order_listForm, UserForm
from .models import Products, User
from .models import Order_list
import csv
import pandas as pd


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
        Products.objects.create(p_id = s["ID"][i],
                                p_name = s["상품명"][i],
                                sale_bar = s["바코드"][i],
                                iq = s["입수"][i],
                                p_price = s["납품가"][i],
                                org_bar = s["원코드"][i],
                                location = s["위치정보"][i])

# 발주등록 order_page
def order_create(request):
    if request.method == 'POST':
        form = Order_listForm(request.POST)
        form_user = UserForm(request.POST)
        if form.is_valid():
            new_order_list = form.save(commit=False)
            new_user = form_user.save(commit=False)
            new_order_list.od_date = timezone.now()
            input_cal = request.POST.get('calender')
            input_buyer = request.POST.get('buyer_select')
            new_order_list.d_day = input_cal
            new_user.buyer_name = input_buyer
            new_order_list.save()
            new_user.save()
            context = {'new_order_list': new_order_list, 'new_user': new_user}
            return render(request, 'eos/order_page_r.html', context)
        else:
            form = Order_listForm(request.POST)
            context = {'form': form}
            return render(request, 'eos/order_page.html', context)
    else:
        form = Order_listForm()
        form_user = UserForm()
        context = {'form': form, 'form_user': form_user}
        return render(request, 'eos/order_page.html', context)

def order_page(request, Order_list_id, User_id):
    new_order_list = get_object_or_404(Order_list, pk=Order_list_id)
    new_user = get_object_or_404(User, pk=User_id)
    context = {'new_order_list': new_order_list, 'new_user': new_user}
    return render(request, 'eos/order_page_r.html', context)


