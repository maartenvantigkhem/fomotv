# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20150531_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address_city',
            new_name='b_address_city',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_countrycode',
            new_name='b_address_countrycode',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_countryname',
            new_name='b_address_countryname',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_state',
            new_name='b_address_state',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_street',
            new_name='b_address_street',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='b_first_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='last_name',
            new_name='b_last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address_zip',
        ),
        migrations.AddField(
            model_name='order',
            name='b_address_zip',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='s_address_city',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='s_address_countrycode',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='s_address_countryname',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='s_address_state',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='s_address_street',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='s_address_zip',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='s_first_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='s_last_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address_flag',
            field=models.BooleanField(default=False),
        ),
    ]
