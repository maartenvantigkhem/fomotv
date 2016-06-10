# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20151018_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='config',
            old_name='first_page_string',
            new_name='first_page_text',
        ),
    ]
