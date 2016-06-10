from django.contrib import admin

# Register your models here.
from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    fields = ['product', 'size', 'color', 'quantity', 'amount']


class OrderAdmin(admin.ModelAdmin):
    """
    Settings for Order Section
    """
    list_display = ['create_date', 'id',  'email', 'b_last_name', 'b_first_name', 'status', 'get_total']
    inlines = [OrderItemInline, ]


admin.site.register(Order, OrderAdmin)
