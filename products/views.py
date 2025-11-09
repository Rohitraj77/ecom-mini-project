from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from core.permissions import IsAdmin

class ProductPublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_deleted=False).order_by("-created_at")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category"]
    search_fields = ["name", "slug"]

class ProductAdminViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]
    queryset = Product.objects.all().order_by("-created_at")
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", "is_deleted"]
    search_fields = ["name", "slug"]

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.is_deleted = True
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
