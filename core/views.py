from django.shortcuts import render
from . import models
from django.http import HttpResponse
import pdb

def index(request, slug=''):
    template_name = 'core/index.html'
    text = models.CoreData.objects.filter(to_publish=True, on_main=True).order_by('usort')
    contex_var = {'text': text}
    # pdb.set_trace()
    return render(request, template_name, contex_var)
