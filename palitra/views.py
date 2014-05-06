# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
 

from pages.models import Page
from slideshow.models import Slider
from vacancy.models import Vacancy
from resumeform.models import Resume
from resumeform.forms import ResumeForm
from staffform.models import Staff
from staffform.forms import StaffForm

import config
from livesettings import config_value
from django.conf import settings
import datetime

PAGINATION_COUNT = 5

def get_common_context(request):
    rform = ResumeForm()
    sform = StaffForm()
    c = {}
    if request.method == 'POST':
        if request.POST['action'] == 'resume':
            rform = ResumeForm(request.POST)
            if rform.is_valid():
                rform.save()
                messages.success(request, u'Ваша заявка успешно отправлена.')
                rform = ResumeForm()
            else:
                messages.error(request, u'Необходимо ввести имя и телефон.')
        elif request.POST['action'] == 'staff':
            sform = StaffForm(request.POST)
            if sform.is_valid():
                sform.save()
                messages.success(request, u'Ваша заявка успешно отправлена.')
                sform = StaffForm()
            else:
                messages.error(request, u'Необходимо ввести имя и телефон.')
        
    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
   
    c['rform'] = rform
    c['sform'] = sform
    c.update(csrf(request))
    return c

def page(request, page_name):
    c = get_common_context(request)
    p = Page.get_by_slug(page_name)
    if p:
        c.update({'p': p})
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    else:
        raise Http404()

def home(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['slider'] = Slider.objects.all()
    c['content'] = Page.get_by_slug('home')
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def vacancy(request):
    c = get_common_context(request)
    #c['slider'] = Slider.objects.all()
    c['content'] = Page.get_by_slug('vacancy')
    return render_to_response('home.html', c, context_instance=RequestContext(request))