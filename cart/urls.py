from django.urls import path
from .import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('test/<int:Cart_id>/', views.cart_test, name='cart_test'),
    path('cart_order_page/', views.cart_order_page, name='cart_order_page'),
]