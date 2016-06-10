# -*- coding: utf-8 -*-
from django.db import models
from main.models import MyUser, Prize


class Order(models.Model):
    #статусы заказа
    TEST_ORDER = 1
    NEW_ORDER = 2
    CONFIRMED_ORDER = 3
    ORDERED_ORDER = 4
    SENT_ORDER = 5
    ARCHIVED_ORDER = 6
    REJECTED_ORDER = 7

    ORDER_STATES = (
        (TEST_ORDER, "Test"),
        (NEW_ORDER, "New"),
        (CONFIRMED_ORDER, "Confirmed"),
        (ORDERED_ORDER, "Ordered"),
        (SENT_ORDER, "Sent"),
        (ARCHIVED_ORDER, "Archived"),
        (REJECTED_ORDER, "Rejected"),
    )

    author = models.ForeignKey(MyUser, blank=True, editable=False, null=True)
    create_date = models.DateTimeField(auto_now=True)
    #person_count

    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    #billing details
    b_first_name = models.CharField(max_length=100, verbose_name="First name")
    b_last_name = models.CharField(max_length=100, verbose_name="Last name")
    b_address_zip = models.CharField(max_length=10, blank=True, null=True, verbose_name="ZIP")
    b_address_countryname = models.CharField(max_length=100, blank=True, null=True, verbose_name="Country name")
    b_address_countrycode = models.CharField(max_length=10, null=True, blank=True, verbose_name="Country code")
    b_address_state = models.CharField(max_length=100, null=True, blank=True, verbose_name="State")
    b_address_city = models.CharField(max_length=100, blank=True, verbose_name="City")
    b_address_street = models.CharField(max_length=200, blank=True, verbose_name="Street")


    #shipping details if
    """
    shipping_address_flag = models.BooleanField(default=False)
    s_first_name = models.CharField(max_length=100, blank=True, null=True)
    s_last_name = models.CharField(max_length=100, blank=True, null=True)
    s_address_zip = models.CharField(max_length=10, blank=True, null=True)
    s_address_countryname = models.CharField(max_length=100, blank=True, null=True)
    s_address_countrycode = models.CharField(max_length=10, null=True, blank=True)
    s_address_state = models.CharField(max_length=100, null=True, blank=True)
    s_address_city = models.CharField(max_length=100, blank=True, null=True)
    s_address_street = models.CharField(max_length=200, blank=True, null=True)
    """
    paypal_transaction_id = models.CharField(max_length=20, null=True, blank=True)

    #product_sum = models.DecimalField(max_digits=8, decimal_places=2)
    #total_sum = models.DecimalField(max_digits=8, decimal_places=2)

    status = models.IntegerField(choices=ORDER_STATES)

    user_comment = models.TextField(blank=True, null=True)
    shop_comment = models.TextField(blank=True, null=True)

    def get_status_name(self):
        if 0 < self.status < 7:
            return self.ORDER_STATUSES[self.status-1][1]
        else:
            return None

    def get_total(self):
        total = 0
        for i in self.items.all():
            total += i.quantity * i.amount
        return round(total, 2)

    @property
    def total(self):
        return self.get_total()


class OrderItem(models.Model):
    """
    Ordered item model
    """
    order = models.ForeignKey('Order', related_name='items')
    product = models.ForeignKey(Prize)
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField() # TODO: add restrictions > 0
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    color = models.CharField(max_length=30, default=None, null=True)
    size = models.CharField(max_length=10, default=None, null=True)

    @property
    def sub_total(self):
        return self.quantity * self.amount
