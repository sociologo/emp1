# Generated by Django 5.1 on 2024-10-02 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0002_alter_prueba_subtitulo_alter_prueba_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prueba',
            name='subtitulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
