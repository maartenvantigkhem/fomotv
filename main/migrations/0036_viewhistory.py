# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20151018_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('competition', models.ForeignKey(to='main.Competition')),
                ('from_user', models.ForeignKey(related_name='viewed_photos', to=settings.AUTH_USER_MODEL)),
                ('photo', models.ForeignKey(related_name='view_history', to='main.Photo')),
            ],
        ),
    ]
