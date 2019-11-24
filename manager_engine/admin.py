from django.contrib import admin
from manager_engine.models import Request, History, Notes
from data_manager.models import Inventory, SalesReport

# Register your models here.
admin.site.register(Request)
admin.site.register(History)
admin.site.register(Notes)

admin.site.register(Inventory)
admin.site.register(SalesReport)
