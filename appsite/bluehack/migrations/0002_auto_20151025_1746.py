# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bluehack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crisisusers',
            name='address',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='crisisusers',
            name='cellphone',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='crisisusers',
            name='user',
            field=models.OneToOneField(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
