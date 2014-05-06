# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'request_date')

admin.site.register(Staff, StaffAdmin)