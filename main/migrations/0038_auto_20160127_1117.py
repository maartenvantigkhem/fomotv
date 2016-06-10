# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20151104_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorTrend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color_name', models.CharField(max_length=100, verbose_name='Name of Color')),
                ('color_hex', models.CharField(max_length=7, verbose_name='Hex of the Color')),
                ('up_votes', models.PositiveIntegerField(null=True)),
                ('down_votes', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DesignSizesTrend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='DesignTrend',
            fields=[
                ('design_ID', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('design_name', models.CharField(max_length=100, verbose_name='Name of the Desgin')),
                ('design_thumbnail', models.ImageField(upload_to=b'designs', verbose_name='Hero Photo')),
            ],
        ),
        migrations.CreateModel(
            name='DesignTrendPhotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('design_photos', models.ImageField(upload_to=b'designs')),
                ('design_ID', models.ForeignKey(to='main.DesignTrend')),
            ],
        ),
        migrations.CreateModel(
            name='UserIDTrend',
            fields=[
                ('user_id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('voter_ip', models.GenericIPAddressField(null=True)),
                ('voter_country', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserVotingTrend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('how_much', models.PositiveIntegerField(null=True)),
                ('nps', models.PositiveIntegerField(null=True)),
                ('design_ID', models.ForeignKey(to='main.DesignTrend')),
                ('preferred_size', models.ForeignKey(to='main.DesignSizesTrend', null=True)),
                ('user_id', models.ForeignKey(to='main.UserIDTrend')),
            ],
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(error_messages={b'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator(b'^[\\s\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', b'invalid')], help_text='Required. 30 characters or fewer.Letters, digits, @/./+/-/_ only', unique=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='winner',
            name='code',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
