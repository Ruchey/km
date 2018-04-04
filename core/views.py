from django.shortcuts import render
from . import models
from django.http import HttpResponse
import pdb

def index(request, slug=''):
    template_name = 'core/index.html'
    html_text = models.CoreData.objects.get(pk=1)
    contex_var = {'html_text': html_text.html_text}
    # pdb.set_trace()
    return render(request, template_name, contex_var)
