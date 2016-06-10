# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20150703_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winner',
            name='photo',
            field=models.ForeignKey(to='main.Photo', null=True),
        ),
    ]
