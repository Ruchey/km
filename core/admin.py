from django.contrib import admin
from django.forms import RadioSelect
from . import models


class CoreDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_publish', 'on_main', 'usort')
    list_editable = ('to_publish', 'on_main', 'usort')
    fieldsets = [
        (None, {'fields': [('title', 'to_publish', 'on_main'), 'text']}),
    ]

admin.site.register(models.CoreData, CoreDataAdmin)
admin.site.register(models.Contacts)