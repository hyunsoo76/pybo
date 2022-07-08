from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Products
import csv
import pandas as pd


def index(request):
    return render(request, 'eos/index.html')

def order_page(request):
    return render(request, 'eos/order_page.html')

class ProductView(ListView):
    model = Products
    template_name = 'eos/product.html'


# 상품db 업데이트
# def p_list(request):
with open("/home/ubuntu/projects/mysite/static/p_list.csv", "r", encoding='cp949') as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []
for i in range(len(s)):
    st = (s["ID"][i], s["상품명"][i], s["바코드"][i], s["입수"][i], s["납품가"][i], s["원코드"][i], s["위치정보"][i])
    ss.append(st)
for i in range(len(ss)):
    Products.objects.create(p_id=int(ss[i][0]), p_name=ss[i][1], sale_bar=int(ss[i][2]),
                            iq=int([i][3]), p_price=int(ss[i][4]), org_bar=int(ss[i][5]), location=ss[i][6])
    # try:
    #     Products.objects.create(p_id=int(ss[i][0]), p_name=ss[i][1], sale_bar=int(ss[i][2]),
    #                             iq=int([i][3]), p_price=int(ss[i][4]), org_bar=int(ss[i][5]), location=ss[i][6])
    #
    # except :
    #     pass