from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import ProductView

app_name = 'eos'

urlpatterns = [
    path('', views.index, name='index'),
    # path('order_page.html/', views.order_page, name='order_page'),
    path('product/', ProductView.as_view(), name='product'),
    path('p_list/', views.p_list),
    # path('order_page/', views.order_page(), name='order_page'),
    path('order_page/', views.order_page(), name='order_create'),
]
