# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_votehistory_vote_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='votehistory',
            name='session',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
