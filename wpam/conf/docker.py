from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',  # set in docker-compose.yml
        'PORT': 5432  # default postgres port
    }
}

CELERY_BROKER_URL = "amqp://guest:guest@mq//"
MEDIA_ROOT = os.path.join('/var/media/')

