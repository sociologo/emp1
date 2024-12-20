# Generated by Django 5.1 on 2024-08-21 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=50, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=20, unique=True, verbose_name='Nombre corto')),
                ('anulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
        ),
    ]
