# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20150526_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='temperature',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'Hot', b'Hot'), (b'Warm', b'Warm'), (b'Mild', b'Mild'), (b'Rain', b'Rain'), (b'Cool', b'Cool'), (b'Cold', b'Cold'), (b'Freezing', b'Freezing')]),
        ),
    ]
