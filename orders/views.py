from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
import csv

from core.permissions import IsAdmin
from .models import Order, ShippingAddress
from .serializers import OrderSerializer, ShippingAddressSerializer

class ShippingAddressViewSet(viewsets.ModelViewSet):
    serializer_class = ShippingAddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-created_at")

class OrderAdminViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]
    queryset = Order.objects.all().order_by("-created_at")
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status","created_at"]
    search_fields = ["id","user__username","user__email"]

    @action(detail=True, methods=["put"], permission_classes=[IsAdmin], url_path="status")
    def update_status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get("status")
        if new_status not in dict(order.STATUS):
            return Response({"error":"invalid status"}, status=400)
        order.status = new_status
        order.save()
        return Response(self.get_serializer(order).data)

    @action(detail=True, methods=["put"], permission_classes=[IsAdmin], url_path="notes")
    def add_note(self, request, pk=None):
        order = self.get_object()
        order.admin_note = request.data.get("note","")
        order.save()
        return Response(self.get_serializer(order).data)

    @action(detail=False, methods=["post"], permission_classes=[IsAdmin], url_path="export")
    def export_csv(self, request):
        ids = request.data.get("ids", [])
        qs = self.get_queryset()
        if ids:
            qs = qs.filter(id__in=ids)

        resp = HttpResponse(content_type="text/csv")
        resp["Content-Disposition"] = "attachment; filename=orders.csv"
        w = csv.writer(resp)
        w.writerow(["OrderID","User","Total","Status","Created"])
        for o in qs:
            w.writerow([o.id, getattr(o.user,"email",""), o.total, o.status, o.created_at])
        return resp
