# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(default=b'Select Gender', max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to=b'series/%Y-%m-%d')),
                ('release', models.DateField()),
                ('review', models.TextField()),
                ('seasons', models.IntegerField()),
                ('actors', models.ManyToManyField(to='Series.actor')),
            ],
        ),
    ]
