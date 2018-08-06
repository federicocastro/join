import raven

from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '',
]

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'beluz'),
        'USER': os.environ.get('DATABASE_USER', 'beluz'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'beluz'),
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
        'OPTIONS': {
        },
    }
}

RAVEN_CONFIG = {
    'dsn': os.environ.get('RAVEN_DSN', ''),
    'release': raven.fetch_git_sha(os.path.dirname(BASE_DIR)),
}
