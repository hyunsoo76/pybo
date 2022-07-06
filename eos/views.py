from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Products


def index(request):
    return render(request, 'eos/index.html')

def order_page(request):
    return render(request, 'eos/order_page.html')

class Productview(ListView):
    model = Products
    template_name = 'product.html'