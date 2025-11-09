from django.contrib import admin
from .models import Product, Order, OrderItem


# Product admin
admin.site.register(Product)

# order admin with inline order items


class OrderItemInline(admin.TabularInline):

    """
    Display order items inline within the order admin.
    """
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price', 'get_total_price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    """
    Admin configuration for the order model.
    """
    list_display = ('id', 'full_name', 'email', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'email', 'id')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [OrderItemInline]
