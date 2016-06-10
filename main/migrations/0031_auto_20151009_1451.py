# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20150822_1956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-create_date']},
        ),
        migrations.AddField(
            model_name='competition',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
