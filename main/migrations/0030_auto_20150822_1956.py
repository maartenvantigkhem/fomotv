# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20150708_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='terms_flag',
            field=models.BooleanField(default=False),
        ),
    ]
