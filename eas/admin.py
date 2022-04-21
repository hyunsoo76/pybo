from django.contrib import admin
from .models import Request

class RquestAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Request, RquestAdmin)