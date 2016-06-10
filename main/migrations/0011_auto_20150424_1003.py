# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_votehistory_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='small_image',
        ),
        migrations.AddField(
            model_name='photo',
            name='active_flag',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='spam_flag',
            field=models.BooleanField(default=False),
        ),
    ]
