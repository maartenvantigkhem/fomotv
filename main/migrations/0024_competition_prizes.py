# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20150612_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='prizes',
            field=models.ManyToManyField(related_name='competitions', through='main.PrizeCompetitionRef', to='main.Prize'),
        ),
    ]
