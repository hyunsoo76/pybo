from django.db import models

class Products(models.Model):
    p_id = models.IntegerField(blank=True, null=True) #상품코드
    org_bar = models.IntegerField(blank=True, null=True) #원코드
    sale_bar = models.IntegerField(blank=True, null=True) #판매코드
    p_name = models.CharField(max_length=200, blank=True) #상품명
    iq = models.IntegerField(blank=True, null=True) #입수
    p_price = models.IntegerField(blank=True, null=True) #출고가
    location = models.CharField(max_length=200, blank=True) #위치정보


class User(models.Model):
    odp_name = models.CharField(max_length=200, blank=True) #발주자명
    buyer_name = models.CharField(max_length=200, blank=True) #수주자명
    phon_num = models.CharField(max_length=200, blank=True) #전화번호


class Order_list(models.Model):
    od_count = models.IntegerField(blank=True, null=True) #낱개발주수량
    od_box_count  = models.IntegerField(blank=True, null=True) #박스발주수량
    d_day = models.DateTimeField(blank=True) #배송요청일
    od_date = models.DateTimeField(blank=True) #발주일(today)
    del_check = models.CharField(max_length=200, blank=True) #미출체크(발주삭제)
    order_note = models.TextField(blank=True) #발주자 기타사항
    out_note = models.TextField(blank=True) #수주자 기타사항
    note = models.TextField(blank=True) #기타사항(공지사항)
    total_sum = models.IntegerField(blank=True, null=True) #발주합계금액
    img1 = models.ImageField(blank=True)
    img2 = models.ImageField(blank=True)
    img3 = models.ImageField(blank=True)
    aaa = models.CharField(max_length=200, blank=True)
    bbb = models.CharField(max_length=200, blank=True)
    ccc = models.CharField(max_length=200, blank=True)
    ddd = models.CharField(max_length=200, blank=True)
    eee = models.CharField(max_length=200, blank=True)
    fff = models.IntegerField(blank=True, null=True)
    ggg = models.IntegerField(blank=True, null=True)
    hhh = models.IntegerField(blank=True, null=True)
    upload = models.FileField(upload_to='uploads/')



