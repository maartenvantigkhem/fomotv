# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_viewhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='winner',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='winner',
            name='prize_group',
            field=models.ForeignKey(related_name='winners', to='main.PrizeGroup', null=True),
        ),
    ]
