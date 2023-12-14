import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from vendor_manage.models import *
import datetime


@pytest.fixture
def apiClient():
  return APIClient()


@pytest.fixture
def authenticate(apiClient):
  def do_authenticate():
    return apiClient.force_authenticate(user=User)
  return do_authenticate


@pytest.fixture
def vendor_set():
  return Vendor.objects.create(
    vendor_code = '1234',
    name = 'Helen',
    address = 'Venus,Germany,433',
    contact_details = '23232'
  )
  
  
@pytest.fixture
def purchase_order_set(vendor_set):
  return Purchase.objects.create(
            po_number=1,
            items={"s":1},
            quantity=4,
            vendor=vendor_set,
            delivery_date=datetime.datetime(2023, 12, 23, 4, 15, 0).strftime("%Y-%m-%dT%H:%M:%SZ"), 
            status='PN',
            issue_date=datetime.datetime(2023, 6, 23, 11, 10, 0).strftime("%Y-%m-%dT%H:%M:%SZ"),
            order_date=datetime.datetime(2023, 6, 23, 5, 12, 0).strftime("%Y-%m-%dT%H:%M:%SZ")
    )
 

@pytest.fixture
def performance_set(vendor_set):
  return HistoricalPerformance.objects.create(
    vendor = vendor_set,
    date = datetime.datetime(2023,12,12,11,2,0).strftime("%Y-%m-%dT%H:%M:%SZ"),
    on_time_delivery_rate = vendor_set.on_time_delivery_rate,
    quality_rating_avg = vendor_set.quality_rating_avg,
    average_response_time = vendor_set.average_response_time,
    fulfillment_rate = vendor_set.fulfillment_rate,
  )
