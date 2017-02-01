# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import versatileimagefield.fields


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
                ('pic', versatileimagefield.fields.VersatileImageField(upload_to=b'actors/%Y-%m-%d', verbose_name=b'actors')),
                ('actors_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', max_length=20, editable=False)),
                ('gender', models.CharField(default=b'Select Gender', max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('pic', versatileimagefield.fields.VersatileImageField(upload_to=b'series/%Y-%m-%d', verbose_name=b'Image')),
                ('series_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', max_length=20, editable=False)),
                ('release', models.DateField()),
                ('review', models.TextField()),
                ('seasons', models.IntegerField()),
                ('actors', models.ManyToManyField(to='Series.actor')),
            ],
        ),
    ]
