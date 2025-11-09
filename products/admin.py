from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "stock", "is_deleted", "created_at")
    list_filter = ("category", "is_deleted")
    search_fields = ("name", "category")
    ordering = ("-created_at",)
