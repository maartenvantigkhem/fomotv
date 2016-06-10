# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_designtrend_design_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignTrendAvailableColors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('design_colors', models.CharField(max_length=6, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='designtrend',
            name='ceil_cost',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='designtrend',
            name='floor_cost',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='designsizestrend',
            name='design_ID',
            field=models.ForeignKey(related_name='sizes', to='main.DesignTrend'),
        ),
        migrations.AlterField(
            model_name='designtrendphotos',
            name='design_ID',
            field=models.ForeignKey(related_name='photos', to='main.DesignTrend'),
        ),
        migrations.AddField(
            model_name='designtrendavailablecolors',
            name='design_ID',
            field=models.ForeignKey(related_name='colors', to='main.DesignTrend'),
        ),
    ]
