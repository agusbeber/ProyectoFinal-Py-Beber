# Generated by Django 4.1.5 on 2023-01-28 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_alter_videojuego_genero'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comprador',
        ),
        migrations.DeleteModel(
            name='Desarrollador',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
    ]
