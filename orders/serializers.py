from rest_framework import serializers
from .models import Order, OrderItem, ShippingAddress
from products.models import Product

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"
        read_only_fields = ["id","user"]

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")
    class Meta:
        model = OrderItem
        fields = ["id","product","product_name","qty","price"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id","user","address","items","total","status","admin_note","created_at"]
        read_only_fields = ["id","user","status","admin_note","created_at","total"]

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        items_data = validated_data.pop("items")
        order = Order.objects.create(user=user, **validated_data)
        total = 0
        for item in items_data:
            product = item["product"]
            qty = item["qty"]
            OrderItem.objects.create(order=order, product=product, qty=qty, price=product.price)
            # reduce stock safely
            product.stock = max(0, product.stock - qty)
            product.save()
            total += product.price * qty
        order.total = total
        order.save()
        return order
