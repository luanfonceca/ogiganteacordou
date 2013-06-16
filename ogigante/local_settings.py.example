DEBUG = True
TEMPLATE_DEBUG = DEBUG

from os.path import abspath, dirname, join

PROJECT_ROOT = dirname(abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ogigante.db',
    }
}

MEDIA_ROOT = join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = join(PROJECT_ROOT, 'static_files')

STATIC_URL = '/static/'
