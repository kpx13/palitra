# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Resume


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'request_date')

admin.site.register(Resume, ResumeAdmin)
