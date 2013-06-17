#encoding: utf-8
from django.forms import ModelForm
from django import forms
from .models import Entry

TIPOS = [
    ('video', u'Vídeo'),
    ('link', 'Link'),
    ('evento', 'Evento')
]

class NewEntryForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('approved', )

    kind = forms.ChoiceField(label='Tipo',choices=TIPOS)