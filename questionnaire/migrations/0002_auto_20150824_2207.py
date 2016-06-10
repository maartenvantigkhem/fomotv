# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['sort_id', 'title']},
        ),
        migrations.AlterField(
            model_name='prizequestionnaireref',
            name='result_code',
            field=models.CharField(max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(upload_to=b'question', null=True, verbose_name='Background image', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='author',
            field=models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='end_flag',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='image',
            field=models.ImageField(upload_to=b'questionnaire', null=True, verbose_name='Background image', blank=True),
        ),
        migrations.AlterField(
            model_name='questionnaireresult',
            name='result_code',
            field=models.CharField(max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E')]),
        ),
        migrations.AlterField(
            model_name='runhistory',
            name='result_code',
            field=models.CharField(max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E')]),
        ),
    ]
