from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .serializers import InventorySerializer, SalesReportSerializer
from .models import Inventory, SalesReport


# Create your views here.

class InventoryView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()


class SalesReportView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = SalesReportSerializer
    queryset = SalesReport.objects.all()
