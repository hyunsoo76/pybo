from django.contrib import admin

from .models import Products, User, Order_list

admin.site.register(Products, User, Order_list)
