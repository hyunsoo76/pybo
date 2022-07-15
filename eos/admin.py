from django.contrib import admin
from .models import Order_list
from .models import Products



class Order_listAdmin(admin.ModelAdmin):
    search_fields = ['d_day']
    search_fields = ['buyer_name']


class ProductsAdmin(admin.ModelAdmin):
    search_fields = ['p_name']
    list_display = ('p_name', 'org_bar', 'sale_bar', 'p_price')

admin.site.register(Order_list, Order_listAdmin)
admin.site.register(Products, ProductsAdmin)

