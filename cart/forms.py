from django import forms
from cart.models import CartItem

class CartForm(forms.ModelForm):
    class Meta:
        model = CartItem  # 사용할 모델
        fields = ['product', 'cart', 'quantity', 'active',
                  ]

