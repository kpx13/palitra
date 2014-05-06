# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

class Vacancy(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name=u'название')
    content = RichTextField(blank=True, verbose_name=u'контент')
        
    class Meta:
        verbose_name = u'вакансия'
        verbose_name_plural = u'вакансии'
        ordering=['id']
        
    def __unicode__(self):
        return str(self.id)
    
