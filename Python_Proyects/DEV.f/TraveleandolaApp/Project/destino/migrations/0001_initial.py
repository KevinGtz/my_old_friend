# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(choices=[('EU', 'ESTADOS UNIDOS'), ('MX', 'MEXICO'), ('AU', 'AUSTRALIA'), ('FR', 'FRANCIA'), ('BR', 'BRASIL'), ('SA', 'SUDAFRICA'), ('SP', 'ESPAÑA')], max_length=100)),
                ('continente', models.CharField(max_length=15)),
                ('imagen', models.ImageField(upload_to='/media/pais/')),
                ('is_active', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
            options={
                'verbose_name': 'Destino',
                'verbose_name_plural': 'Destinos',
            },
        ),
    ]
