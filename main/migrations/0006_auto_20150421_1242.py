# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150417_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=7, verbose_name='Color HTML Code')),
            ],
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='prize',
            field=models.ForeignKey(related_name='photos', to='main.Prize'),
        ),
        migrations.AddField(
            model_name='prize',
            name='colors',
            field=models.ManyToManyField(related_name='products', to='main.ProductColor'),
        ),
    ]
