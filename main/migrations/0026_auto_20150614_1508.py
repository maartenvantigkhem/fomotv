# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20150612_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added'),
        ),
    ]
