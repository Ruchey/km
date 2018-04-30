from django.contrib import admin
from django.forms import RadioSelect
from . import models


class CoreDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_publish', 'to_menu', 'usort')
    list_editable = ('to_publish', 'to_menu', 'usort')
    fieldsets = [
        (None, {'fields': [('title', 'to_publish'), 'to_menu', 'text']}),
    ]


admin.site.register(models.CoreData, CoreDataAdmin)
admin.site.register(models.Contacts)
