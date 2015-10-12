# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crisis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('alert_level', models.CharField(max_length=200)),
                ('event_id', models.IntegerField()),
                ('created_date', models.DateTimeField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('geo_lat', models.FloatField()),
                ('geo_long', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CrisisUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notified', models.BooleanField(default=False)),
                ('evacuating', models.BooleanField(default=False)),
                ('responded', models.BooleanField(default=False)),
                ('crisis', models.ForeignKey(to='bluehack.Crisis')),
            ],
        ),
    ]
