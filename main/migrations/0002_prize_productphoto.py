# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name of Product')),
                ('retail_price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('discount_amount', models.IntegerField()),
                ('sale_price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('sizes', models.CharField(max_length=5, choices=[(b'XXS', b'XXS'), (b'XS', b'XS')])),
                ('size_types', models.CharField(max_length=4, choices=[(b'US', b'US'), (b'UK', b'UK'), (b'EU', b'EU'), (b'Asia', b'Asia')])),
                ('measurement_chart', models.FileField(upload_to=b'measurement_chart')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'product_photo', verbose_name='Photo')),
                ('prize', models.ForeignKey(to='main.Prize')),
            ],
        ),
    ]
