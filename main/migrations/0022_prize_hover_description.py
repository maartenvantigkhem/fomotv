# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20150527_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='hover_description',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
