from django.db import models

class Request(models.Model):
    create_date = models.DateTimeField(blank=True)
    select_form = models.CharField(max_length=200, blank=True)
    subject = models.CharField(max_length=200)
    a_1 = models.CharField(max_length=200)
    a_2 = models.CharField(max_length=200, blank=True)
    a_3 = models.CharField(max_length=200, blank=True)
    a_4 = models.CharField(max_length=200, blank=True)
    a_5 = models.IntegerField()
    a_6 = models.CharField(max_length=200, blank=True)
    a_7 = models.CharField(max_length=200, blank=True)
    b_1 = models.CharField(max_length=200, blank=True)
    b_2 = models.CharField(max_length=200, blank=True)
    b_3 = models.CharField(max_length=200, blank=True)
    b_4 = models.CharField(max_length=200, blank=True)
    b_5 = models.IntegerField(blank=True, null=True)
    b_6 = models.CharField(max_length=200, blank=True)
    b_7 = models.CharField(max_length=200, blank=True)
    c_1 = models.CharField(max_length=200, blank=True)
    c_2 = models.CharField(max_length=200, blank=True)
    c_3 = models.CharField(max_length=200, blank=True)
    c_4 = models.CharField(max_length=200, blank=True)
    c_5 = models.IntegerField(blank=True, null=True)
    c_6 = models.CharField(max_length=200, blank=True)
    c_7 = models.CharField(max_length=200, blank=True)
    d_1 = models.CharField(max_length=200, blank=True)
    d_2 = models.CharField(max_length=200, blank=True)
    d_3 = models.CharField(max_length=200, blank=True)
    d_4 = models.CharField(max_length=200, blank=True)
    d_5 = models.IntegerField(blank=True, null=True)
    d_6 = models.CharField(max_length=200, blank=True)
    d_7 = models.CharField(max_length=200, blank=True)
    e_1 = models.CharField(max_length=200, blank=True)
    e_2 = models.CharField(max_length=200, blank=True)
    e_3 = models.CharField(max_length=200, blank=True)
    e_4 = models.CharField(max_length=200, blank=True)
    e_5 = models.IntegerField(blank=True, null=True)
    e_6 = models.CharField(max_length=200, blank=True)
    e_7 = models.CharField(max_length=200, blank=True)
    f_1 = models.CharField(max_length=200, blank=True)
    f_2 = models.CharField(max_length=200, blank=True)
    f_3 = models.CharField(max_length=200, blank=True)
    f_4 = models.CharField(max_length=200, blank=True)
    f_5 = models.IntegerField(blank=True, null=True)
    f_6 = models.CharField(max_length=200, blank=True)
    f_7 = models.CharField(max_length=200, blank=True)
    g_1 = models.CharField(max_length=200, blank=True)
    g_2 = models.CharField(max_length=200, blank=True)
    g_3 = models.CharField(max_length=200, blank=True)
    g_4 = models.CharField(max_length=200, blank=True)
    g_5 = models.IntegerField(blank=True, null=True)
    g_6 = models.CharField(max_length=200, blank=True)
    g_7 = models.CharField(max_length=200, blank=True)
    h_1 = models.CharField(max_length=200, blank=True)
    h_2 = models.CharField(max_length=200, blank=True)
    h_3 = models.CharField(max_length=200, blank=True)
    h_4 = models.CharField(max_length=200, blank=True)
    h_5 = models.IntegerField(blank=True, null=True)
    h_6 = models.CharField(max_length=200, blank=True)
    h_7 = models.CharField(max_length=200, blank=True)
    i_1 = models.CharField(max_length=200, blank=True)
    i_2 = models.CharField(max_length=200, blank=True)
    i_3 = models.CharField(max_length=200, blank=True)
    i_4 = models.CharField(max_length=200, blank=True)
    i_5 = models.IntegerField(blank=True, null=True)
    i_6 = models.CharField(max_length=200, blank=True)
    i_7 = models.CharField(max_length=200, blank=True)
    j_1 = models.CharField(max_length=200, blank=True)
    j_2 = models.CharField(max_length=200, blank=True)
    j_3 = models.CharField(max_length=200, blank=True)
    j_4 = models.CharField(max_length=200, blank=True)
    j_5 = models.IntegerField(blank=True, null=True)
    j_6 = models.CharField(max_length=200, blank=True)
    j_7 = models.CharField(max_length=200, blank=True)
    chamjo1 = models.TextField(blank=True)
    jisi1 = models.TextField(blank=True)
    total = models.IntegerField(blank=True, null=True)
    date1 = models.DateTimeField(null=True, blank=True)
    date2 = models.DateTimeField(null=True, blank=True)
    date3 = models.DateTimeField(null=True, blank=True)
    dojang1 = models.ImageField(blank = True)
    dojang2 = models.ImageField(blank = True)
    dojang3 = models.ImageField(blank = True)
    aaa = models.CharField(max_length=200,blank=True) #이사결재
    bbb = models.CharField(max_length=200, blank=True) #대표이사결재
    ccc = models.CharField(max_length=200, blank=True) #상신버튼체크
    ddd = models.CharField(max_length=200, blank=True) #이사결재체크
    eee = models.CharField(max_length=200, blank=True)
    fff = models.IntegerField(blank=True, null=True)
    ggg = models.IntegerField(blank=True, null=True)
    hhh = models.IntegerField(blank=True, null=True)





    def __str__(self):
        return self.subject