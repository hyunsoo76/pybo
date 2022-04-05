from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/eas/', views.detail, name='detail'),
]