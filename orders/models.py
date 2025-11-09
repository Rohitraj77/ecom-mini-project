
from django.db import models
from django.conf import settings
from products.models import Product

class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    country = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.line1}, {self.city}"

class Order(models.Model):
    STATUS = (
        ("Pending","Pending"),
        ("Processing","Processing"),
        ("Shipped","Shipped"),
        ("Delivered","Delivered"),
        ("Cancelled","Cancelled"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    admin_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
