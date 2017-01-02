# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=14)),
                ('ubicacion', models.CharField(max_length=50)),
                ('raiting', models.PositiveIntegerField()),
                ('imagenes', models.ImageField(upload_to=b'')),
                ('precio', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('num_jugadores', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Reta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horario', models.DateTimeField()),
                ('precio', models.PositiveIntegerField()),
                ('tipo_reta', models.CharField(max_length=50)),
            ],
        ),
    ]
