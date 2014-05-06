# -*- coding: utf-8 -*-

from django.db import models
from dashboard import string_with_title


class Staff(models.Model):
    name  = models.CharField(u'Имя', max_length=255)
    phone  = models.CharField(u'Телефон', blank=True, max_length=255)
    email  = models.CharField(u'Email', blank=True, max_length=255)
    comment  = models.CharField(u'Комментарий', blank=True, max_length=255)
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = u'заявка на подбор персонала'
        verbose_name_plural = u'заявки на подбор персонала'
        app_label = string_with_title("staffform", u"Заявки на подбор персонала")
        ordering = ['-request_date']
        
    
    def __unicode__(self):
        return str(self.name)

