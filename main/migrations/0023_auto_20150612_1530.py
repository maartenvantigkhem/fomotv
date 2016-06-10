# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_prize_hover_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrizeCompetitionRef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prize_type', models.CharField(max_length=2, choices=[(b'rv', b'Random vote'), (b'bp', b'Best photo')])),
            ],
        ),
        migrations.RemoveField(
            model_name='competition',
            name='best_photo_prize',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='prizes',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='random_voter_prize',
        ),
        migrations.AddField(
            model_name='prizecompetitionref',
            name='competition',
            field=models.ForeignKey(to='main.Competition'),
        ),
        migrations.AddField(
            model_name='prizecompetitionref',
            name='prize',
            field=models.ForeignKey(to='main.Prize'),
        ),
    ]
