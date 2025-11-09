from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import ShippingAddress, Order, OrderItem

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "line1", "city", "state", "zip", "country")
    search_fields = ("user__username", "line1", "city")

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # one empty row by default

def export_orders_csv(modeladmin, request, queryset):
    """
    Admin action: export selected orders as CSV.
    """
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=orders.csv"
    writer = csv.writer(response)
    writer.writerow(["OrderID", "User", "Total", "Status", "Created At"])
    for o in queryset:
        writer.writerow([o.id, getattr(o.user, "username", ""), o.total, o.status, o.created_at])
    return response

export_orders_csv.short_description = "Export selected orders to CSV"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("id", "user__username", "user__email")
    inlines = [OrderItemInline]
    actions = [export_orders_csv]  # <-- the new CSV action

    # Recalculate total when items are edited inline
    def save_formset(self, request, form, formset, change):
        instances = formset.save()
        order = form.instance
        total = 0
        for item in order.items.all():
            total += (item.price or 0) * (item.qty or 0)
        order.total = total
        order.save()
