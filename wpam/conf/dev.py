from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

    }
}

CELERY_BROKER_URL = "amqp://guest:guest@172.17.0.2:5672//"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
