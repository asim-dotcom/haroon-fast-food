from django.contrib import admin

# Register your models here.


from .models import Category, FoodItem, Order, OrderItem


admin.site.register(Category)
admin.site.register(FoodItem)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = (
        "food_item",
        "item_name",
        "quantity",
        "unit_price",
        "line_total",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "customer_name",
        "customer_phone",
        "total",
        "payment_method",
        "payment_timing",
        "status",
        "created_at",
    )
    list_filter = ("status", "payment_method", "payment_timing", "created_at")
    search_fields = ("reference", "customer_name", "customer_phone")
    readonly_fields = (
        "reference",
        "subtotal",
        "delivery_charge",
        "total",
        "created_at",
    )
    date_hierarchy = "created_at"
    inlines = [OrderItemInline]