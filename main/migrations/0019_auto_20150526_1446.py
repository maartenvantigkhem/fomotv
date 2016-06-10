# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20150516_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=250L)),
                ('view_flag', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='prize',
            name='temperature',
            field=models.CharField(default=None, max_length=20, choices=[(b'Hot', b'Hot'), (b'Warm', b'Warm'), (b'Mild', b'Mild'), (b'Rain', b'Rain'), (b'Cool', b'Cool'), (b'Cold', b'Cold'), (b'Freezing', b'Freezing')], null=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prize',
            name='sizes',
            field=select_multiple_field.models.SelectMultipleField(max_length=100, choices=[(b'One size', b'One size'), (b'XXS', b'XXS'), (b'XS', b'XS'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'2', b'2'), (b'4', b'4'), (b'6', b'6'), (b'8', b'8'), (b'10', b'10'), (b'12', b'12'), (b'14', b'14'), (b'16', b'16')]),
        ),
        migrations.AddField(
            model_name='prize',
            name='category',
            field=models.ForeignKey(blank=True, to='main.Category', null=True),
        ),
    ]
