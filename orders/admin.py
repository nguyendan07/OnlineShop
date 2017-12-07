from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    mode = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


# Register your models here.
admin.site.register(Order, OrderAdmin)
