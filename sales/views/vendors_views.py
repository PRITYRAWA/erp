from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models.vendors import Vendor, VendorAddress, VendorProducts
from ..serializers.vendors_serializers import VendorAddressSerializer, VendorProductsSerializer, VendorSerializer
from django_filters.rest_framework import DjangoFilterBackend


class VendorViewSet(viewsets.ModelViewSet):
    """
    API’s endpoint that allows Vendors to be modified.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("__all__")
    ordering_fields = ("__all__")
    

class VendorAddressViewSet(viewsets.ModelViewSet):
    queryset = VendorAddress.objects.all()
    serializer_class = VendorAddressSerializer

class VendorProductsViewSet(viewsets.ModelViewSet):
    queryset = VendorProducts.objects.all()
    serializer_class = VendorProductsSerializer