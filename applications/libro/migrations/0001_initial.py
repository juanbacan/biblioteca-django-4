# Generated by Django 4.0.6 on 2022-07-15 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicación')),
                ('portada', models.ImageField(upload_to='portadas')),
                ('numero_paginas', models.PositiveIntegerField()),
                ('visitas', models.PositiveIntegerField(default=0)),
                ('autores', models.ManyToManyField(to='autor.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.categoria')),
            ],
        ),
    ]