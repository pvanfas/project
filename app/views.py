from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json


def dashboard(request):
    context = {
        'is_dashboard' : True,
        'is_need_chart' : True
    }
    return render(request, 'app/index.html',context)


def buttons(request):
    return render(request,'app/pages/buttons.html',)
def elements(request):
    context = {'is_need_file_upload' : True}
    return render(request,'app/pages/elements.html',)
def table(request):
    return render(request,'app/pages/table.html',)
def chart(request):
    context = {'is_need_chart' : True}
    return render(request,'app/pages/chart.html',context)
def icons(request):
    return render(request,'app/pages/icons.html',)
def typography(request):
    return render(request,'app/pages/typography.html',)
