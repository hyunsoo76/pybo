from django.contrib import admin
from .models import Cart
from .models import CartItem



class CartAdmin(admin.ModelAdmin):
    search_fields = ['cart_id', 'date_added']


class CartItemAdmin(admin.ModelAdmin):
    search_fields = ['product', 'cart']
    list_display = ('product', 'cart', 'quantity', 'active')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

