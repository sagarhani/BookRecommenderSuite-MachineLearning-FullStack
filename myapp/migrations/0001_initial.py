# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=15)),
                ('author', models.CharField(max_length=120)),
                ('year', models.CharField(max_length=15)),
                ('genre_name', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.IntegerField()),
                ('gname', models.CharField(max_length=30)),
            ],
        ),
    ]
