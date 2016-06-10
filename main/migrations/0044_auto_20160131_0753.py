# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20160131_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservotingtrend',
            name='preferred_size',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
