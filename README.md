# emp1

Éste es el primer proyecto django basado en el curso Udemy.

Los hemos diseñado asi:

Hemos creados dos carpeta. Una con nuestros entornos **mis_entornos** y el segundo con nuestros proyectos **mis_proyectos**, donde alojaremos el proyecto **emp1**.

Lo que hacemos es tener los entornos separados de los proyectos. Atención con ésto porque el proyecto que desplegaremos en el servidor droplet de DigitalOcean será diferente. En él instalaremos nuestro proyecto dentro de la carpeta de entornos.

Desplegamos nuestro proyecto en local así:

```
C:\>cd mis_entornos
C:\mis_entornos>cd entorno_1/Scripts
C:\mis_entornos\entorno_1\Scripts>activate
(entorno_1) C:\mis_entornos\entorno_1\Scripts>
(entorno_1) C:\mis_entornos\entorno_1\Scripts>cd /
(entorno_1) C:\>
(entorno_1) C:\mis_proyectos\emp1>python manage.py runserver --settings=empleado.settings.local
```

El archivo **local.py** es:

```bash
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

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
```

Desplegamos nuestro proyecto en el servidor así:
```
C:\Windows\System32>ssh christian1@164.92.107.9
password: xxxxxxxxxx

christian1@django:/$ cd /mis_proyectos/entorno_1
christian1@django:/mis_proyectos/entorno_1$ source bin/activate
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ cd emp1
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ sudo supervisorctl restart empleado
```

El archivo **prod.py** es:

```bash
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bded6',
        'USER ': 'christian1',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / 'media'
```









