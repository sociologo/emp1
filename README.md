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
