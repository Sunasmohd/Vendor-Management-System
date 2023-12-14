from django.db import models
from django.core.validators import MinValueValidator


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(primary_key=True,max_length=100)
    on_time_delivery_rate = models.FloatField(default=0,validators=[MinValueValidator(0)]) # Tracks the percentage of on-time deliveries.
    quality_rating_avg = models.FloatField(default=0,validators=[MinValueValidator(0)]) # Average rating of quality based on purchase orders.
    average_response_time = models.FloatField(default=0,validators=[MinValueValidator(0)]) # Average time taken to acknowledge purchase orders.
    fulfillment_rate = models.FloatField(default=0,validators=[MinValueValidator(0)]) # Percentage of purchase orders fulfilled successfully


CHOICES_STATUS = [
  ('PN','Pending'),('CN','Canceled'),('CM','Completed')
]    


class Purchase(models.Model):
    po_number = models.CharField(primary_key=True,max_length=100)
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,related_name="purchase_order",null=True)
    order_date = models.DateTimeField() #Date when the order was placed.
    delivery_date = models.DateTimeField() #Expected delivery date of the order.
    items = models.JSONField() #Details of items ordered.
    quantity = models.IntegerField(validators=[MinValueValidator(0)]) #Total quantity of items in the PO.
    status = models.CharField(max_length=2,choices=CHOICES_STATUS) #Current status of the PO (e.g : pending, completed, canceled).
    quality_rating = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0)]) #Rating given to the vendor for this PO (nullable).
    issue_date = models.DateTimeField() #Timestamp when the PO was issued to the vendor.
    acknowledgment_date = models.DateTimeField(null=True,blank=True) #Nullable - Timestamp when the vendor acknowledged the PO
    
    
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='performance') #Link to the Vendor model.
    date = models.DateTimeField(unique=True)  #Date of the performance record.
    on_time_delivery_rate = models.FloatField(validators=[MinValueValidator(0)]) #Historical record of the on-time delivery rate.
    quality_rating_avg =  models.FloatField(validators=[MinValueValidator(0)]) #Historical record of the quality rating average.
    average_response_time =  models.FloatField(validators=[MinValueValidator(0)]) #Historical record of the average response time.
    fulfillment_rate = models.FloatField(validators=[MinValueValidator(0)])  #Historical record of the fullfilment rate.