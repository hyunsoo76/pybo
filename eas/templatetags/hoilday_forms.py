from django import forms
from eas.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request  # 사용할 모델
        fields = ['create_date',
                  'select_form',
                  'subject',
                  'a_1', 'a_5', 'b_1', 'c_1', 'd_1', 'e_1',   'f_1', 'f_2', 'f_3', 'f_4', 'f_5', 'f_6', 'f_7',
                  'g_1', 'g_2', 'g_3', 'g_4', 'g_5', 'g_6', 'g_7',
                  'h_1', 'h_2', 'h_3', 'h_4', 'h_5', 'h_6', 'h_7',
                  'i_1', 'i_2', 'i_3', 'i_4', 'i_5', 'i_6', 'i_7',
                  'j_1', 'j_2', 'j_3', 'j_4', 'j_5', 'j_6', 'j_7',
                  'chamjo1', 'jisi1', 'total', 'date1', 'date2',
                  'date3', 'dojang1', 'dojang2', 'dojang3',
                  'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg',
                  'hhh']
