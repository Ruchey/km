from django.contrib import admin
from django.forms import RadioSelect
from . import models


class CoreDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_publish', 'to_menu', 'usort')
    list_editable = ('to_publish', 'to_menu', 'usort')
    fieldsets = [
        (None, {'fields': [('title', 'to_publish'), 'to_menu', 'text']}),
    ]

class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'to_publish', 'is_main', 'usort')
    list_editable = ('to_publish', 'usort')
    fieldsets = [
        (None, {'fields': ['title', 'slug', 'to_publish', 'is_main', 'usort']}),
    ]


admin.site.register(models.CoreData, CoreDataAdmin)
admin.site.register(models.Contacts)
admin.site.register(models.MainMenu, MainMenuAdmin)