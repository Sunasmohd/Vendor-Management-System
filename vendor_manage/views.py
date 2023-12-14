from rest_framework.viewsets import ModelViewSet
from .models import Vendor,Purchase,HistoricalPerformance
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render


class VendorModelViewSet(ModelViewSet):
  queryset = Vendor.objects.all()
  serializer_class = VendorSerializer
  
  
class PurchaseModelViewSet(ModelViewSet):
  queryset = Purchase.objects.all()
  serializer_class = PurchaseSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['vendor_id']
  
  
class HistoricalPerformanceModelViewSet(ModelViewSet):
  
  def get_queryset(self):
     return HistoricalPerformance.objects.filter(vendor_id=self.kwargs.get('vendors_pk'))
  
  def get_serializer_class(self):
    if self.request.method == 'POST':
      return CreateHistoricalPerformanceSerializer
    return HistoricalPerformanceSerializer
  
  def create(self, request, *args, **kwargs):
    serializer = CreateHistoricalPerformanceSerializer(
        data=request.data,
      )
    serializer.is_valid(raise_exception=True)
    history = serializer.save(vendor_id=self.kwargs.get('vendors_pk'))
    serializer = HistoricalPerformanceSerializer(history)
    return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
class AcknowledgeViewSet(ModelViewSet):
    http_method_names = ('post','head','options')
    queryset = Purchase.objects.all()
    serializer_class = AcknowledgeSerializer
    
    def get_queryset(self):
       return Purchase.objects.filter(po_number=self.kwargs.get('purchase_orders_pk'))
  
    def create(self, request, **kwargs):
        purchase_order = Purchase.objects.get(po_number = kwargs.get('purchase_orders_pk'))
        serializer = AcknowledgeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        acknowledgment_date = serializer.validated_data['acknowledgment_date']
        purchase_order.acknowledgment_date = acknowledgment_date
        purchase_order.save()
        serializer = PurchaseSerializer(purchase_order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)