from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'core.views.index', name='index'),
    url(r'^eventos$', 'core.views.events', name='events'),
    url(r'^novo$', 'core.views.new_entry', name='new_entry'),
    url(r'^admin/', include(admin.site.urls)),

)
