from django.shortcuts import render
from django.views import generic
from . import models

import pdb


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'coredata_text'
    # pdb.set_trace()

    def get_queryset(self):
        return models.CoreData.objects.filter(to_publish=True, to_menu=1).order_by('usort')

# def index(init):
#     pdb.set_trace()
    
#     text = models.CoreData.objects.filter(to_publish=True, on_main=True).order_by('usort')
#     contex_var = {'text': text}
    
#     return render(request, template_name, contex_var)
