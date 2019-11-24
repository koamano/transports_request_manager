from django.db import models
from datetime import datetime


class Inventory(models.Model):
    category = models.CharField(max_length=32)
    itemNumber = models.CharField(max_length=128)
    itemName = models.CharField(max_length=128)
    vendor = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    onHandCollege = models.IntegerField(default=0)
    onHandSolano = models.IntegerField(default=0)
    price = models.FloatField()
    gender = models.CharField(max_length=32)
    subCategory = models.CharField(max_length=32, default=' ')
    style = models.CharField(max_length=32, default='normal')
    size = models.CharField(max_length=32)
    width = models.CharField(max_length=32, default='NA')

    def __str__(self):
        return f"{self.itemNumber}"


class SalesReport(models.Model):
    store = models.CharField(max_length=128, default='none')
    customerName = models.CharField(max_length=128)
    category = models.CharField(max_length=32)
    itemNumber = models.CharField(max_length=128)
    itemName = models.CharField(max_length=128)
    vendor = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    numberSold = models.IntegerField()
    unitPrice = models.FloatField()
    sellPrice = models.FloatField()
    gender = models.CharField(max_length=32)
    subCategory = models.CharField(max_length=32, default=' ')
    style = models.CharField(max_length=32, default='normal')
    size = models.CharField(max_length=32)
    width = models.CharField(max_length=3, default='NA')
    dateSold = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.itemNumber}"
