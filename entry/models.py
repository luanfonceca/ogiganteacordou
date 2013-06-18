#coding: utf-8
from django.db import models
from core.models import TimeStampedModel

EntryTypes = [
    ('link', u'Link'),
    ('video', u'Vídeo'),
    ('evento', u'Evento')
]


class Entry(TimeStampedModel):
    kind = models.CharField(
        u'Tipo', default='link', max_length=400, choices=EntryTypes
    )
    title = models.CharField(u'Título', max_length=400)
    text = models.CharField(u'Texto', max_length=400)
    approved = models.BooleanField(u'Aprovado')

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return u'<Entry [{}] {}>'.format(self.kind, self.title)

    def is_video(self):
        return self.kind == 'video'
