from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from .models import Cart, CartItem
from django.shortcuts import render, get_object_or_404, redirect
from .models import Products


#     cart view
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(_cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request, total=0,counter=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.p_price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart/cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def cart_test(request, Cart_id, cart_item=None):
    cart = get_object_or_404(Cart, pk=Cart_id)
    cart_items = CartItem.objects.filter(cart=cart, active=True)
    esum = (cart_item.product.p_price * cart_item.quantity)
    return render(request, 'eos/order_list.html', dict(cart_items=cart_items, esum=esum))