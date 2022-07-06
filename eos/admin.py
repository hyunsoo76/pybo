from django.contrib import admin

from .models import Order_list
from .models import User





class Order_listAdmin(admin.ModelAdmin):
    search_fields = ['d_day']

class UserAdmin(admin.ModelAdmin):
    search_fields = ['buyer_name']

class Products(admin.ModelAdmin):
    search_fields = ['p_name']

admin.site.register(Order_list, Order_listAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Products, UserAdmin)