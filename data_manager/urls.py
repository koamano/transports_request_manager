from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'inventory', views.InventoryView, 'inventory')
router.register(r'salesreport', views.SalesReportView, 'salesReport')

urlpatterns = [
    path('', include(router.urls)),
]
