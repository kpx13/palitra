# -*- coding: utf-8 -*-
 
from django.forms import ModelForm
from models import Staff
from django.conf import settings
from livesettings import config_value
from django.core.mail import send_mail
from django.template import Context, Template

def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        [config_value('MyApp', 'EMAIL')])


class StaffForm(ModelForm):    
    class Meta:
        model = Staff
        exclude = ('date', )
      
    def save(self, *args, **kwargs):
        super(StaffForm, self).save(*args, **kwargs)
        subject=u'Новая заявка на подбор персонала'
        
        body_templ="""
{% for field in form %}
   {{ field.label }} - {{ field.value }}
{% endfor %}
            """
        ctx = Context({
            'form': self,

        })
        body = Template(body_templ).render(ctx)
        sendmail(subject, body)

