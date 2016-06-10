# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_competition_prizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 18, 55, 20, 13000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prize',
            name='website_link',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
