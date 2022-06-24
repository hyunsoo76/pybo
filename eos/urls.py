from django.urls import path
from . import views

app_name = 'eos'

urlpatterns = [
    path('', views.index, name='index'),
]