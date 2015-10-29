# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bluehack', '0002_auto_20151025_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrisisUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cellphone', models.CharField(default=b'', max_length=10)),
                ('address', models.CharField(default=b'', max_length=100)),
                ('notified', models.BooleanField(default=False)),
                ('evacuating', models.BooleanField(default=False)),
                ('responded', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='crisisusers',
            name='crisis',
        ),
        migrations.RemoveField(
            model_name='crisisusers',
            name='user',
        ),
        migrations.DeleteModel(
            name='CrisisUsers',
        ),
    ]
