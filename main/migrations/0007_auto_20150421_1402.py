# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150421_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prize',
            old_name='size_types',
            new_name='size_type',
        ),
    ]
