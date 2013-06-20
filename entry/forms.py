#encoding: utf-8
from django.forms import ModelForm, TextInput
from .models import Entry


class NewEntryForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('approved', 'fixed',)
        widgets = {
            'title': TextInput(attrs={'class': 'span4'}),
            'text': TextInput(attrs={'class': 'span4'}),
        }
