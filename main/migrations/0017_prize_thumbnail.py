# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20150513_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='thumbnail',
            field=models.ImageField(default='', upload_to=b'prize', verbose_name='Thumbnail'),
            preserve_default=False,
        ),
    ]
