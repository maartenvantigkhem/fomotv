# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20151009_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('refresh_week_day', models.CharField(default=b'3', max_length=1, choices=[(b'1', b'Monday'), (b'2', b'Tuesday'), (b'3', b'Wednesday'), (b'4', b'Thursday'), (b'5', b'Friday'), (b'6', b'Saturday'), (b'7', b'Sunday')])),
                ('first_page_string', models.TextField(default=b'')),
            ],
        ),
        migrations.AlterModelOptions(
            name='prize',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='prizegroup',
            name='prizes',
            field=models.ManyToManyField(related_name='groups', through='main.PrizeGroupRef', to='main.Prize'),
        ),
    ]
