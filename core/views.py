#coding: utf-8
from entry.models import Entry
from django.shortcuts import render, redirect
from entry.forms import NewEntryForm
from recaptcha.client import captcha
from django.conf import settings


def index(request):
    context = {}
    context['entries'] = Entry.objects.filter(
        approved=True).order_by('-pub_date')
    return render(request, 'index.html', context)


def all_entries(request):
    context = {}
    context['entries'] = Entry.objects.all().order_by('-pub_date')
    context['show_status'] = True
    return render(request, 'index.html', context)


def events(request):
    context = {}
    context['entries'] = Entry.objects.filter(approved=True).order_by(
        '-pub_date')
    return render(request, 'events.html', context)


def new_entry(request):
    context = {}
    form = NewEntryForm(request.POST or None)
    context['form'] = form
    resp = captcha.submit(
        request.POST.get('recaptcha_challenge_field'),
        request.POST.get('recaptcha_response_field'),
        settings.RECAPTCHA_SECRET,
        request.META['REMOTE_ADDR']
    )
    if resp and form.is_valid():
        entry = form.save()
        entry.save()
        context['form'] = NewEntryForm()
        context['success'] = True

    return render(request, 'new_entry.html', context)
