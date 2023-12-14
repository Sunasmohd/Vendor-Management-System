from rest_framework import serializers
from .models import Vendor,Purchase,HistoricalPerformance
from djoser.serializers import UserCreateSerializer as UCS,UserSerializer as US
from django.core.exceptions import ValidationError


class VendorSerializer(serializers.ModelSerializer):
  on_time_delivery_rate = serializers.FloatField(read_only=True)
  quality_rating_avg = serializers.FloatField(read_only=True)
  average_response_time = serializers.FloatField(read_only=True)
  fulfillment_rate = serializers.FloatField(read_only=True)
  
  class Meta:
    model = Vendor
    fields = [
      'name',
      'contact_details',
      'address',
      'vendor_code',
      'on_time_delivery_rate',
      'quality_rating_avg',
      'average_response_time',
      'fulfillment_rate',
    ]
    
    
class PurchaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Purchase
    fields = [
      'po_number',
      'vendor',
      'order_date',
      'delivery_date',
      'items',
      'quantity',
      'status',
      'quality_rating',
      'issue_date',
      'acknowledgment_date'
    ]
    
    
  def validate(self,data):
    errors = []
    
    if data.get('acknowledgment_date') and data.get('acknowledgment_date') < data.get('issue_date'):
        errors.append('acknowledgment_date should be greater than issue_date')
        
    if data.get('acknowledgment_date') and data.get('acknowledgment_date') < data.get('order_date'):
        errors.append('acknowledgment_date should be greater than order_date')
        
    if data.get('delivery_date') < data.get('order_date'):
        errors.append('delivery_date should be greater than order_date')
        
    if data.get('delivery_date') < data.get('issue_date'):
        errors.append('delivery_date should be greater than issue_date')
        
    if data.get('acknowledgment_date') and data.get('acknowledgment_date') > data.get('delivery_date') :
        errors.append('delivery_date should be greater than acknowledgment_date')
        
    if data.get('issue_date') < data.get('order_date'):
        errors.append('issue_date should be greater than order_date')
        
    if errors:
        message = {}
        message['errors'] = errors
        raise ValidationError(message)  
      
    return data
      
      
class HistoricalPerformanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = HistoricalPerformance
    fields = [
      'id',
      'vendor',
      'date',
      'on_time_delivery_rate',
      'quality_rating_avg',
      'average_response_time',
      'fulfillment_rate'
    ]
    
    
class CreateHistoricalPerformanceSerializer(serializers.ModelSerializer):
  vendor = serializers.IntegerField(read_only=True)
  class Meta:
    model = HistoricalPerformance
    fields = [
      'vendor',
      'date',
    ]    
  
  def save(self,vendor_id, **kwargs):
    vendor = Vendor.objects.get(vendor_code = vendor_id)
    return HistoricalPerformance.objects.create(
            vendor_id = vendor_id,
            on_time_delivery_rate = vendor.on_time_delivery_rate,    
            quality_rating_avg = vendor.quality_rating_avg,                                  
            average_response_time = vendor.average_response_time,                                  
            fulfillment_rate = vendor.fulfillment_rate,                                  
            **self.validated_data
          )


class AcknowledgeSerializer(serializers.Serializer):
    acknowledgment_date = serializers.DateTimeField()
    

class UserCreateSerializer(UCS):
  class Meta(UCS.Meta):
    fields = ['id','username','password']
    

class UserSerializer(US):
  class Meta(US.Meta):
    fields = ['id','username']