import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'join.settings.local')

from django.conf import settings

if not settings.DEBUG:
    import celery
    import raven
    from raven.contrib.celery import register_signal, register_logger_signal

    class Celery(celery.Celery):

        def on_configure(self):
            dsn = getattr(settings, 'RAVEN_CONFIG', {}).get('dsn', '')
            client = raven.Client(dsn)
            register_logger_signal(client)
            register_signal(client)
else:
    from celery import Celery

app = Celery()

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
