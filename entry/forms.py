#encoding: utf-8
from django.forms import ModelForm
from django import forms
from .models import Entry

class NewEntryForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('approved', )
