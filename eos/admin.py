from django.contrib import admin

from .models import Order_list
from .models import User

admin.site.register(Order_list)
admin.site.register(User)