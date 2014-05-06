# -*- coding: utf-8 -*-
 
from django.forms import ModelForm, fields, TextInput
from models import Resume
from django.conf import settings
from livesettings import config_value
from django.core.mail import send_mail
from django.template import Context, Template

def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        [config_value('MyApp', 'EMAIL')])


class ResumeForm(ModelForm):    
    
    name  = fields.CharField(label=u'Имя', widget=TextInput(attrs={'placeholder': u'Ваше имя'}))
    email  = fields.CharField(label=u'E-mail', widget=TextInput(attrs={'placeholder': u'E-mail'}))
    phone  = fields.CharField(label=u'Телефон', required=False, widget=TextInput(attrs={'placeholder': u'Телефон'}))
    
    class Meta:
        model = Resume
        exclude = ('date', )
      
    def save(self, *args, **kwargs):
        super(ResumeForm, self).save(*args, **kwargs)
        subject=u'Новое резюме'
        
        body_templ="""

   Имя - {{ form.name.value }}
   Email - {{ form.email.value }}
   Телефон - {{ form.phone.value }}
   Файл: - http://palitra.webgenesis.ru/uploads/resumes/{{ form.file.value }}

            """
            
        ctx = Context({
            'form': self,
        })
        body = Template(body_templ).render(ctx)
        sendmail(subject, body)
