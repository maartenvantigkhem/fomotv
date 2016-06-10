# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150424_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='competition',
            field=models.ForeignKey(related_name='all_photos', verbose_name='Competition', to='main.Competition'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='discount_amount',
            field=models.IntegerField(help_text=b'Discount in percent (%), only numbers, ie 15', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='prize',
            name='sale_price',
            field=models.DecimalField(max_digits=9, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='votehistory',
            name='photo',
            field=models.ForeignKey(related_name='vote_history', to='main.Photo'),
        ),
    ]
