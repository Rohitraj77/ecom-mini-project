from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShippingAddressViewSet, OrderViewSet, OrderAdminViewSet

router = DefaultRouter()
router.register(r"addresses", ShippingAddressViewSet, basename="address")
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"admin/orders", OrderAdminViewSet, basename="order-admin")

urlpatterns = [path("", include(router.urls))]
