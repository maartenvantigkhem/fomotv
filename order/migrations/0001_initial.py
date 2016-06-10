# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20150516_1123'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address_zip', models.CharField(max_length=10, blank=True)),
                ('address_countryname', models.CharField(max_length=10, blank=True)),
                ('address_countrycode', models.CharField(max_length=10, blank=True)),
                ('address_state', models.CharField(max_length=100, blank=True)),
                ('address_city', models.CharField(max_length=100, blank=True)),
                ('address_street', models.CharField(max_length=200, blank=True)),
                ('paypal_transaction_id', models.CharField(max_length=20, blank=True)),
                ('status', models.IntegerField(choices=[(1, b'Test'), (2, b'New'), (3, b'Confirmed'), (4, b'Ordered'), (5, b'Sent'), (6, b'Archived'), (7, b'Rejected')])),
                ('user_comment', models.TextField(null=True, blank=True)),
                ('shop_comment', models.TextField(null=True, blank=True)),
                ('author', models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('order', models.ForeignKey(related_name='items', to='order.Order')),
                ('product', models.ForeignKey(to='main.Prize')),
            ],
        ),
    ]
