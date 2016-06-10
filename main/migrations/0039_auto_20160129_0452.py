# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20160127_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colortrend',
            name='id',
        ),
        migrations.AlterField(
            model_name='colortrend',
            name='color_hex',
            field=models.CharField(max_length=7, serialize=False, verbose_name='Hex of the Color', primary_key=True),
        ),
    ]
