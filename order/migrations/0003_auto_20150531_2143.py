# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20150524_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_countryname',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
