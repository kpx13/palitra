# -*- coding: utf-8 -*-
from django.db import models
from dashboard import string_with_title

class Slider(models.Model):
    image = models.ImageField(upload_to= 'uploads/slider', max_length=256, verbose_name=u'картинка')
    order = models.IntegerField(blank=True, null=True, verbose_name=u'порядок сортировки', help_text=u'№ слайдера: 1й, 2й .. 5й')
    
    class Meta:
        verbose_name = 'слайдер'
        verbose_name_plural = 'слайдер'
        app_label = string_with_title("slideshow", u"Слайдшоу")
        ordering = ['order']
        
    
    def __unicode__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        super(Slider, self).save(*args, **kwargs)
        if not self.order:
            self.order = self.id
            self.save()