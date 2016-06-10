# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20160131_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useridtrend',
            name='voter_country',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
