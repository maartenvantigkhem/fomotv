# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20150614_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('prize_type', models.CharField(max_length=2, choices=[(b'rv', b'Random vote'), (b'bp', b'Best photo')])),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='end_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='winner',
            name='competition',
            field=models.ForeignKey(to='main.Competition'),
        ),
        migrations.AddField(
            model_name='winner',
            name='photo',
            field=models.ForeignKey(to='main.Photo'),
        ),
        migrations.AddField(
            model_name='winner',
            name='prize',
            field=models.ForeignKey(to='main.Prize', null=True),
        ),
        migrations.AddField(
            model_name='winner',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
