# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150501_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='purchase_price',
            field=models.DecimalField(default=10, max_digits=9, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prize',
            name='sizes',
            field=select_multiple_field.models.SelectMultipleField(max_length=1000, choices=[(b'XXS', b'XXS'), (b'XS', b'XS'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'2', b'2'), (b'4', b'4'), (b'6', b'6'), (b'8', b'8'), (b'10', b'10'), (b'12', b'12'), (b'14', b'14'), (b'16', b'16')]),
        ),
    ]
