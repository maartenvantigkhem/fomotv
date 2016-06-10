# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20160131_0101'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='uservotingtrend',
            unique_together=set([('design_ID', 'user_id')]),
        ),
    ]
