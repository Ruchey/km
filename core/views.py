from django.shortcuts import render

from django.http import HttpResponse


def index(request, slug=''):
    template_name = 'core/index.html'
    return render(request, template_name)
