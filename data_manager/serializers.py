from rest_framework import serializers
from .models import Inventory, SalesReport


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            'category',
            'itemNumber',
            'itemName',
            'vendor',
            'color',
            'onHandCollege',
            'onHandSolano',
            'price',
            'gender',
            'subCategory',
            'style',
            'size',
            'width'
        )


class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = (
            'store',
            'customerName',
            'category',
            'itemNumber',
            'itemName',
            'vendor',
            'color',
            'numberSold',
            'unitPrice',
            'sellPrice',
            'gender',
            'subCategory',
            'style',
            'size',
            'width',
            'dateSold',

        )
