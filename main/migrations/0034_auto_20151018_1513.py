# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20151018_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='name',
            field=models.CharField(default=b'Website settings', max_length=100),
        ),
        migrations.AlterField(
            model_name='config',
            name='first_page_string',
            field=models.TextField(default=b'<h2 id="numero6"><a href="" ng-click="selectPhotoFromDesktop()">Enter a photo</a> or <a href="">vote</a></h2><h4>in photo competitions to win one of these prizes:</h4>'),
        ),
    ]
