# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20150822_1956'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.BooleanField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrizeQuestionnaireRef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result_code', models.CharField(max_length=1, choices=[(b'A', b'Yes'), (b'B', b'No'), (b'C', b'Partially')])),
                ('prize', models.ForeignKey(to='main.Prize')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name='Name of Questionnaire')),
                ('image', models.ImageField(upload_to=b'question', null=True, verbose_name='Background image')),
                ('sort_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='Name of Questionnaire')),
                ('title', models.CharField(max_length=200, verbose_name='Longer Title')),
                ('image', models.ImageField(upload_to=b'questionnaire', null=True, verbose_name='Background image')),
                ('active_flag', models.BooleanField(default=True, verbose_name='Is Active')),
                ('top_flag', models.BooleanField(default=False, verbose_name='Show on First page')),
                ('end_date', models.DateField(null=True)),
                ('end_flag', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('prizes', models.ManyToManyField(related_name='questionnaires', through='questionnaire.PrizeQuestionnaireRef', to='main.Prize')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionnaireResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('yes_percent', models.IntegerField()),
                ('result_code', models.CharField(max_length=1, choices=[(b'A', b'Yes'), (b'B', b'No'), (b'C', b'Partially')])),
                ('questionnaire', models.ForeignKey(related_name='results', to='questionnaire.Questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='RunHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result_code', models.CharField(max_length=1, choices=[(b'A', b'Yes'), (b'B', b'No'), (b'C', b'Partially')])),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('questionnaire', models.ForeignKey(to='questionnaire.Questionnaire')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(related_name='questions', to='questionnaire.Questionnaire'),
        ),
        migrations.AddField(
            model_name='prizequestionnaireref',
            name='questionnaire',
            field=models.ForeignKey(to='questionnaire.Questionnaire'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='questionnaire.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='questionnaire',
            field=models.ForeignKey(to='questionnaire.Questionnaire'),
        ),
    ]
