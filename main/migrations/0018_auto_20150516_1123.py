# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_prize_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='abuse_reason',
            field=models.CharField(blank=True, max_length=20, choices=[(b'content', b'PHOTO FROM ANOTHER SOURCE'), (b'inappropriate', b'INAPPROPRIATE PHOTO'), (b'notrelevant', b'NOT RELEVENT TO THE CONTEST'), (b'spam', b'THIS IS A SPAM !')]),
        ),
        migrations.AlterField(
            model_name='prize',
            name='size_type',
            field=models.CharField(max_length=100, choices=[(b'US', b'US'), (b'UK', b'UK'), (b'EU', b'EU'), (b'Asia', b'Asia')]),
        ),
        migrations.AlterField(
            model_name='prize',
            name='sizes',
            field=select_multiple_field.models.SelectMultipleField(max_length=100, choices=[(b'XXS', b'XXS'), (b'XS', b'XS'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'2', b'2'), (b'4', b'4'), (b'6', b'6'), (b'8', b'8'), (b'10', b'10'), (b'12', b'12'), (b'14', b'14'), (b'16', b'16')]),
        ),
    ]
