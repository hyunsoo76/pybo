from django.db import models


class Pay_list(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=30)
    base_pay = models.IntegerField()
    overtime_pay = models.IntegerField(null=True, blank=True)
    holiday_pay = models.IntegerField(null=True, blank=True)
    meal_cost = models.IntegerField(null=True, blank=True)
    car_fee = models.IntegerField(null=True, blank=True)
    incentive1 = models.IntegerField(null=True, blank=True)
    incentive2 = models.IntegerField(null=True, blank=True)
    total_pay = models.IntegerField()
    tax = models.IntegerField(null=True, blank=True)
    local_tax = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    longterm_care = models.IntegerField(null=True, blank=True)
    National_Pension = models.IntegerField(null=True, blank=True)
    Employment = models.IntegerField(null=True, blank=True)
    deduction_sum = models.IntegerField()
    payment = models.IntegerField()
    etc_explain = models.TextField()

    def __str__(self):
        return self.name