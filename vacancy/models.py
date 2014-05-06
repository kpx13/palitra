# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from dashboard import string_with_title

class Vacancy(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name=u'название')
    content = RichTextField(blank=True, verbose_name=u'контент')
    order = models.IntegerField(blank=True, null=True, verbose_name=u'порядок сортировки', help_text=u'№ вакансии: 1й, 2й .. 5й')
        
    class Meta:
        verbose_name = u'вакансия'
        verbose_name_plural = u'вакансии'
        app_label = string_with_title("vacancy", u"Вакансии")
        ordering = ['order']
        
    def __unicode__(self):
        return str(self.id)
    

    def save(self, *args, **kwargs):
        super(Vacancy, self).save(*args, **kwargs)
        if not self.order:
            self.order = self.id
            self.save()