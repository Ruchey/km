from django.contrib import admin

from . import models

class CoreDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_publish')
    fieldsets = [
        (None, {'fields': [('title', 'to_publish'), 'html_text']}),
    ]

admin.site.register(models.CoreData, CoreDataAdmin)