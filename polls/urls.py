from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index),

    path('<int:pay_list_id>/',
         views.detail, name='detail')

]