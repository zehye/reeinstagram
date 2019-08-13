from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'base.json')))

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.dev.application'

DATABASES = secrets['DATABASES']

INSTALLED_APPS += [
    '',
]
