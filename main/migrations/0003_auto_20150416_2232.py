# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_prize_productphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='discount_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='prize',
            name='measurement_chart',
            field=models.FileField(upload_to=b'measurement_chart', blank=True),
        ),
        migrations.AlterField(
            model_name='prize',
            name='size_types',
            field=models.CharField(max_length=1000, choices=[(b'US', b'US'), (b'UK', b'UK'), (b'EU', b'EU'), (b'Asia', b'Asia')]),
        ),
        migrations.AlterField(
            model_name='prize',
            name='sizes',
            field=select_multiple_field.models.SelectMultipleField(max_length=1000, choices=[(b'XXS', b'XXS'), (b'XS', b'XS')]),
        ),
    ]
