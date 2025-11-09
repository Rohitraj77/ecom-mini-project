from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductPublicViewSet, ProductAdminViewSet

router = DefaultRouter()
router.register(r"products", ProductPublicViewSet, basename="product-public")
router.register(r"admin/products", ProductAdminViewSet, basename="product-admin")

urlpatterns = [path("", include(router.urls))]
