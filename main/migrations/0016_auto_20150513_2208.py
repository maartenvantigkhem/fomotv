# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20150508_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='terms_flag',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='competition',
            name='active_flag',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='best_photo_prize',
            field=models.ForeignKey(related_name='best_prizes', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='main.Prize', null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='random_voter_prize',
            field=models.ForeignKey(related_name='random_voters', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='main.Prize', null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='top_flag',
            field=models.BooleanField(default=False, verbose_name='Show on First page'),
        ),
    ]
