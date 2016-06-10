# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20151009_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrizeGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.SlugField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PrizeGroupRef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prize_type', models.CharField(max_length=2, choices=[(b'rv', b'Random vote'), (b'bp', b'Best photo')])),
                ('group', models.ForeignKey(to='main.PrizeGroup')),
                ('prize', models.ForeignKey(to='main.Prize')),
            ],
        ),
        migrations.AddField(
            model_name='prizegroup',
            name='prizes',
            field=models.ManyToManyField(to='main.Prize', through='main.PrizeGroupRef'),
        ),
    ]
