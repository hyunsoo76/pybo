from django.shortcuts import render
from django.http import HttpResponse
import django.shortcuts.render

# Create your views here.
def index(request):
    return render(request, 'polls/main.html')