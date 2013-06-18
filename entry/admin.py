from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'approved', )
    model = Entry
    ordering = ['approved']

admin.site.register(Entry, EntryAdmin)
