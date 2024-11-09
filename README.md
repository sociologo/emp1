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
(entorno_1) C:\mis_proyectos\emp1>python manage.py runserver
```
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
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ python3 manage.py runserver 0.0.0.0:8000
```

164.92.107.9:8000

Para bajar el puerto 8000:
```
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ sudo lsof -i -P -n | grep LISTEN
systemd        1            root   68u  IPv6    6515      0t0  TCP *:22 (LISTEN)
systemd-r    675 systemd-resolve   15u  IPv4    6213      0t0  TCP 127.0.0.53:53 (LISTEN)
systemd-r    675 systemd-resolve   17u  IPv4    6215      0t0  TCP 127.0.0.54:53 (LISTEN)
sshd         982            root    3u  IPv6    6515      0t0  TCP *:22 (LISTEN)
postgres    2852        postgres    6u  IPv6   16674      0t0  TCP [::1]:5432 (LISTEN)
postgres    2852        postgres    7u  IPv4   16675      0t0  TCP 127.0.0.1:5432 (LISTEN)
nginx     199082            root    7u  IPv4 1316366      0t0  TCP *:80 (LISTEN)
nginx     199082            root    8u  IPv6 1316367      0t0  TCP *:80 (LISTEN)
nginx     199083        www-data    7u  IPv4 1316366      0t0  TCP *:80 (LISTEN)
nginx     199083        www-data    8u  IPv6 1316367      0t0  TCP *:80 (LISTEN)
python3   229926      christian1    3u  IPv4 1591811      0t0  TCP *:8000 (LISTEN)
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ sudo kill -9 229926
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ python3 manage.py runserver 0.0.0.0:8000
```

El archivo local.py en el servidor queda:
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
        'PORT': '',
    }
}

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / ("media")
```
