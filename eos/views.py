from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'eos/index.html')

def oredr_page(request):
    return render(request, 'eos/order_page.html')