# Generated by Django 4.1.5 on 2023-01-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='genero',
            field=models.CharField(choices=[('accion', 'Acción'), ('aventura', 'Aventura'), ('estrategia', 'Estrategia'), ('rol', 'Rol'), ('simulacion', 'Simulación'), ('otro', 'Otro')], max_length=15),
        ),
    ]
