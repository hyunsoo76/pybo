from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'eos'

urlpatterns = [
    path('', views.index, name='index'),
]