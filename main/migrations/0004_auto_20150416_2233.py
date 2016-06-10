# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150416_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='discount_amount',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
