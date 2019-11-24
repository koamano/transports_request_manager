from rest_framework import generics, permissions
from rest_framework.response import Response


class InventoryLoadAPI(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        return "uploaded"
