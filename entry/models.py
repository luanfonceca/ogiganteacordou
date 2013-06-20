#coding: utf-8
from django.db import models
from core.models import TimeStampedModel
import urlparse

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
    fixed = models.BooleanField(u'Fixo')

    class Meta:
        ordering = ['-fixed', '-pub_date']

    def __unicode__(self):
        return u'[{0}] {1} '.format(self.kind, self.title)

    def is_video(self):
        return self.kind == 'video'

    @property
    def get_video_id(self):
        return self.text.split('/')[4]
