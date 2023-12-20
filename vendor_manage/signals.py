from .models import Purchase,Vendor
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from django.db.models import Avg
from decimal import Decimal


@receiver(post_save,sender=Purchase)
def get_on_time_delivery_rate(sender,instance,**kwargs):
    if instance.status == 'CM':
      actual_delivery_date = datetime.today().date()
      
      completed_po = Purchase.objects.filter(
        vendor=instance.vendor, status='CM'
      ).count()
      
      on_time_delivered_po = Purchase.objects.filter(
        vendor=instance.vendor, status='CM', delivery_date__gte = actual_delivery_date
      ).count()
      
      calculated_time = round(Decimal((on_time_delivered_po/completed_po) * 10 ),2)
      
      Vendor.objects.filter(
        vendor_code=instance.vendor_id
      ).update(on_time_delivery_rate=calculated_time)

    
@receiver(post_save,sender=Purchase)
def get_quality_rating_average(sender,instance,**kwargs):
    if instance.status == 'CM':
      
      total_qr = Purchase.objects.filter(
        vendor = instance.vendor,status = 'CM'
      )
      
      avg_qr = total_qr.aggregate(Avg('quality_rating'))
      
      if avg_qr['quality_rating__avg'] is not None:
        avg_qr_rounded = round(Decimal(avg_qr['quality_rating__avg']),2)
        
        Vendor.objects.filter(
          vendor_code=instance.vendor_id
        ).update(quality_rating_avg=avg_qr_rounded)
      
    
@receiver(post_save,sender=Purchase)
def get_average_response_time(sender,instance,**kwargs):
    if instance.acknowledgment_date is not None:
      purchase_orders = Purchase.objects.filter(vendor_id=instance.vendor_id)

      response_time = [(
        (po.acknowledgment_date - po.issue_date).total_seconds() /60 /60
        ) 
          for po in purchase_orders if po.acknowledgment_date != None
        ]
      average_response_time = round(Decimal(sum(response_time) / len(response_time)),2) if response_time else None
      
      if average_response_time is not None:
        Vendor.objects.filter(
          vendor_code=instance.vendor_id
        ).update(average_response_time = average_response_time)

        
@receiver(post_save,sender=Purchase)
def get_fullfilment_rate(sender,instance,**kwargs):
    if instance.status == 'CM' or instance.status == 'CN':
      total_po = Purchase.objects.filter(vendor=instance.vendor).count()

      completed_po = Purchase.objects.filter(
        vendor_id=instance.vendor_id,status='CM'
      ).count()
      
      Vendor.objects.filter(
        vendor_code=instance.vendor_id
      ).update(fulfillment_rate=round(Decimal((completed_po/total_po) * 10),2))    