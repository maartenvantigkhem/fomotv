# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20160129_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='designsizestrend',
            name='design_ID',
            field=models.ForeignKey(default=1, to='main.DesignTrend'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='designsizestrend',
            name='sizes',
            field=models.CharField(default='XS', max_length=4),
            preserve_default=False,
        ),
    ]
