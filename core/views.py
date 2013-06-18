#coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from recaptcha.client import captcha

from entry.models import Entry
from entry.forms import NewEntryForm


def index(request):
    context = {}

    entries = Entry.objects.filter(approved=True)
    entries = entries.order_by('-pub_date')

    paginator = Paginator(entries, 25)

    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    context['entries'] = entries
    return render(request, 'index.html', context)


def all_entries(request):
    context = {}
    context['entries'] = Entry.objects.all().order_by('-pub_date')
    context['show_status'] = True
    return render(request, 'index.html', context)


def events(request):
    context = {}
    context['entries'] = Entry.objects.filter(approved=True, kind='evento').order_by(
        '-pub_date')
    return render(request, 'events.html', context)


def new_entry(request):
    context = {}
    form = NewEntryForm(request.POST or None)
    context['form'] = form

    if request.method == 'POST':
        resp = captcha.submit(
            request.POST.get('recaptcha_challenge_field'),
            request.POST.get('recaptcha_response_field'),
            settings.RECAPTCHA_SECRET,
            request.META['REMOTE_ADDR']
        )

        if resp.is_valid and form.is_valid():
            entry = form.save()
            entry.save()
            context['form'] = NewEntryForm()
            messages.error(request, u"Recebemos o seu envio, "
                                    u"em breve as informação "
                                    u"estarão disponíveis para todos.")
        else:
            messages.error(request, u"Houve um problema com o seu envio, "
                                    u"tente novamente.")
    return render(request, 'new_entry.html', context)

def erro404(request):
    return render(request, '404.html')

def entry(request, entry_pk):
    entry = get_object_or_404(Entry, pk=int(entry_pk))

    return render(request, 'entry.html', locals())
