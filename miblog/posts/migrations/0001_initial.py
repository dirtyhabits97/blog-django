# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.CharField(max_length=500)),
                ('fecha_pub', models.DateTimeField(verbose_name='date published')),
                ('categoria', models.CharField(choices=[('TE', 'Tecnolog\xeda'), ('AC', 'Actualidad'), ('PO', 'Pol\xedtica'), ('EN', 'Entretenimiento')], default='AC', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('usuario', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='usuario_pub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Usuario'),
        ),
    ]