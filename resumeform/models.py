# -*- coding: utf-8 -*-

from django.db import models
from pytils import translit

class Resume(models.Model):
    name  = models.CharField(u'Имя', max_length=255)
    phone  = models.CharField(u'Телефон', max_length=255)
    email  = models.CharField(u'Email', blank=True, max_length=255)
    file = models.FileField(upload_to=lambda instance, filename: 'uploads/resumes/' + translit.translify(filename), 
                            max_length=256, verbose_name=u'файл')
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = u'резюме'
        verbose_name_plural = u'резюме'
        ordering = ['-request_date']
    
    def __unicode__(self):
        return str(self.name)

