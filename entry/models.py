#coding: utf-8
from django.db import models
from core.models import TimeStampedModel


class Entry(TimeStampedModel):
    kind = models.CharField(u'Tipo', default='link', max_length=400)
    title = models.CharField(u'Título', max_length=400)
    text = models.CharField(u'Texto', max_length=400)
    approved = models.BooleanField(u'Aprovado')

    def __unicode__(self):
        return '<Entry [{}] {}>'.format(self.kind, self.title)
