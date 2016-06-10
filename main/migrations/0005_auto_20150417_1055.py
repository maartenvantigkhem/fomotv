# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150416_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCompetitionRef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_count', models.IntegerField(default=0, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoteHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('vote_count', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='prizes',
            field=models.ManyToManyField(to='main.Prize'),
        ),
        migrations.AddField(
            model_name='votehistory',
            name='competition',
            field=models.ForeignKey(to='main.Competition'),
        ),
        migrations.AddField(
            model_name='votehistory',
            name='from_user',
            field=models.ForeignKey(related_name='votes_given', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='votehistory',
            name='photo',
            field=models.ForeignKey(to='main.Photo'),
        ),
        migrations.AddField(
            model_name='votehistory',
            name='to_user',
            field=models.ForeignKey(related_name='votes_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercompetitionref',
            name='competition',
            field=models.ForeignKey(to='main.Competition'),
        ),
        migrations.AddField(
            model_name='usercompetitionref',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='competition',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='main.UserCompetitionRef'),
        ),
    ]
