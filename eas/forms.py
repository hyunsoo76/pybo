from django import forms
from eas.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request  # 사용할 모델
        fields = ['create_date',
                  'select_form',
                  'subject',
                  'a_1', 'a_2', 'a_3', 'a_4', 'a_5', 'a_6', 'a_7',
                  'b_1', 'b_2', 'b_3', 'b_4', 'b_5', 'b_6', 'b_7',
                  'c_1', 'c_2', 'c_3', 'c_4', 'c_5', 'c_6', 'c_7',
                  'd_1', 'd_2', 'd_3', 'd_4', 'd_5', 'd_6', 'd_7',
                  'e_1', 'e_2', 'e_3', 'e_4', 'e_5', 'e_6', 'e_7',
                  'f_1', 'f_2', 'f_3', 'f_4', 'f_5', 'f_6', 'f_7',
                  'g_1', 'g_2', 'g_3', 'g_4', 'g_5', 'g_6', 'g_7',
                  'h_1', 'h_2', 'h_3', 'h_4', 'h_5', 'h_6', 'h_7',
                  'i_1', 'i_2', 'i_3', 'i_4', 'i_5', 'i_6', 'i_7',
                  'j_1', 'j_2', 'j_3', 'j_4', 'j_5', 'j_6', 'j_7',
                  'chamjo1', 'jisi1', 'total', 'date1', 'date2',
                  'date3', 'dojang1', 'dojang2', 'dojang3',
                  'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg',
                  'hhh']
