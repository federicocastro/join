from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'beluz_test'),
        'USER': os.environ.get('DATABASE_USER', 'beluz'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'beluz'),
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
        'OPTIONS': {
        },
    }
}
