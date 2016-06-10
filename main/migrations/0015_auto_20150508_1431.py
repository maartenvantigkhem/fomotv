# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20150504_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='active_flag',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='top_flag',
            field=models.BooleanField(default=False),
        ),
    ]
