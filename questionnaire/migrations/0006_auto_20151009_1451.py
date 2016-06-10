# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0005_runhistory_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runhistory',
            name='questionnaire',
            field=models.ForeignKey(related_name='history', to='questionnaire.Questionnaire'),
        ),
        migrations.AlterField(
            model_name='runhistory',
            name='result',
            field=models.ForeignKey(related_name='history', to='questionnaire.QuestionnaireResult', null=True),
        ),
    ]
