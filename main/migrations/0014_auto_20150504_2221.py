# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150503_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='number',
            field=models.CharField(default='', max_length=100, verbose_name='Product Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='competition',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name of Competition'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='prizes',
            field=models.ManyToManyField(related_name='competitions', to='main.Prize'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='sale_price',
            field=models.IntegerField(blank=True),
        ),
    ]
