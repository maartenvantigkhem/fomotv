# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150422_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='votehistory',
            name='vote_type',
            field=models.CharField(default='V', max_length=1, choices=[(b'V', b'Vote'), (b'S', b'Share')]),
            preserve_default=False,
        ),
    ]
