from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'approved', 'fixed')
    model = Entry
    ordering = ['-fixed', 'approved']

admin.site.register(Entry, EntryAdmin)
