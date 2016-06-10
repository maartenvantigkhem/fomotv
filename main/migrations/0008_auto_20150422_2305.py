# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150421_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='best_photo_prize',
            field=models.ForeignKey(related_name='best_prizes', blank=True, to='main.Prize', null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='random_voter_prize',
            field=models.ForeignKey(related_name='random_voters', blank=True, to='main.Prize', null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='competition',
            field=models.ForeignKey(related_name='photos', verbose_name='Competition', to='main.Competition'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='small_image',
            field=models.ImageField(upload_to=b'photo/small', verbose_name='Small photo', blank=True),
        ),
    ]
