from .base import *

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.local.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_URL = '/media/'
MEDIA_DIR = os.path.join(ROOT_DIR, '.media')
