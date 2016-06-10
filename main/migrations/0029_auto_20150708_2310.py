# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20150703_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='delivery_time',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='prize',
            name='shipping_cost',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='winner',
            name='competition',
            field=models.ForeignKey(related_name='winners', to='main.Competition'),
        ),
    ]
