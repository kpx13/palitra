# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class VAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Vacancy, VAdmin)