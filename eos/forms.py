from django import forms
from eos.models import Order_list
from cart.models import CartItem

class Order_listForm(forms.ModelForm):
    class Meta:
        model = Order_list  # 사용할 모델
        fields = ['od_count', 'od_box_count', 'd_day', 'od_date',
                  'del_check', 'order_note', 'out_note', 'note',
                  'total_sum', 'img1', 'img2', 'img3', 'aaa',
                  'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'upload',
                  'buyer_name', 'odp_name', 'phon_num', 'od_list', 's_iq',
                  's_price', 's_location', 's_org_bar']

