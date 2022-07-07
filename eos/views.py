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

with open("/static/p_list.csv", "r") as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []
for i in range(len(s)):
    st = (s["ID"][i], s["상품명"][i], s["바코드"][i], s["입수"][i], s["납품가"][i], s["원코드"][i])
    ss.append(st)
for i in range(len(s)):
    Products.objects.create(name=ss[i][0], code=ss[i][1], ipo_date=ss[i][2])