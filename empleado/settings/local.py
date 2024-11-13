from .base import *

DEBUG = True

ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = ['https://sociolab.cl']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER ': 'chris',
        'PASSWORD': 'nueva123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / ("media")
