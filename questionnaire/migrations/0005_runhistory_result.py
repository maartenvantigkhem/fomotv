# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20150825_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='runhistory',
            name='result',
            field=models.ForeignKey(to='questionnaire.QuestionnaireResult', null=True),
        ),
    ]
