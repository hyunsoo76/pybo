
from django.shortcuts import render
from .models import Pay_list

def index(request):
    """
    paystub 목록 출력
    """
    # 조회
    pay_list = Pay_list.objects.order_by('-id')

    # pay_list = pay_list
    context = {'pay_list': pay_list}
    return render(request, 'paystub/main.html', context)

def detail(request, pay_list_id):
    """
    paystub 목록 출력
    """
    # 조회
    pay_list = Pay_list.objects.get(id=pay_list_id)

    # pay_list = pay_list
    context = {'pay_list': pay_list}
    return render(request, 'paystub/main_detail.html', context)

