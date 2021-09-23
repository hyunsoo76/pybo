from django.db import models


class Pay_list(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=30)
    base_pay = models.IntegerField()
    overtime_pay = models.IntegerField()
    holiday_pay = models.IntegerField()
    meal_cost = models.IntegerField()
    car_fee = models.IntegerField()
    incentive1 = models.IntegerField()
    incentive2 = models.IntegerField()
    total_pay = models.IntegerField()
    tax = models.IntegerField()
    local_tax = models.IntegerField()
    health = models.IntegerField()
    longterm_care = models.IntegerField()
    National_Pension = models.IntegerField()
    Employment = models.IntegerField()
    deduction_sum = models.IntegerField()
    payment = models.IntegerField()
    etc_explain = models.TextField()

    # def __str__(self):
    #     return self.name