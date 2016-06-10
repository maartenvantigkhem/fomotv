# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20160130_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='designtrend',
            name='design_description',
            field=models.TextField(null=True),
        ),
    ]
