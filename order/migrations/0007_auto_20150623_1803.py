# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20150622_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='s_address_city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='s_address_countrycode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='s_address_countryname',
        ),
        migrations.RemoveField(
            model_name='order',
            name='s_address_state',
        ),
        migrations.RemoveField(
            model_name='order',
            name='s_address_street',
        ),
        migrations.RemoveField(
            model_name='order',
            name='s_address_zip',
        ),
        migrations.RemoveField(
            model_name='order',
            name='s_first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='s_last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address_flag',
        ),
        migrations.AlterField(
            model_name='order',
            name='b_address_city',
            field=models.CharField(max_length=100, verbose_name=b'City', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='b_address_countrycode',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Country code', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='b_address_countryname',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Country name', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='b_address_state',
            field=models.CharField(max_length=100, null=True, verbose_name=b'State', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='b_address_street',
            field=models.CharField(max_length=200, verbose_name=b'Street', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='b_address_zip',
            field=models.CharField(max_length=10, null=True, verbose_name=b'ZIP', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='b_first_name',
            field=models.CharField(max_length=100, verbose_name=b'First name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='b_last_name',
            field=models.CharField(max_length=100, verbose_name=b'Last name'),
        ),
    ]
