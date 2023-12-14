import pytest
from rest_framework import status
import datetime
from vendor_manage.models import *
import json


#This function returns endpoints based on the http method
@pytest.fixture
def create_purchase_order(apiClient,purchase_order_set):
  def do_create_purchase_order(purchase_obj,method=None):
    if method == 'p':
      return apiClient.put(f'/api/purchase_orders/{purchase_order_set.pk}/',purchase_obj)
    elif method == 'd':
      return apiClient.delete(f'/api/purchase_orders/{purchase_order_set.pk}/')
    elif method == 'ga':
      return apiClient.get(f'/api/purchase_orders/')
    elif method == 'g':
      return apiClient.get(f'/api/purchase_orders/{purchase_order_set.pk}/')
    else:
      return apiClient.post('/api/purchase_orders/',purchase_obj)
  return do_create_purchase_order
    

@pytest.mark.django_db
class TestPurchaseOrder:
  
  def test_if_user_is_anonymous_returns_401(self,create_purchase_order):
    response1 = create_purchase_order({'po_number':''})
    response2 = create_purchase_order({},'ga')
    response3 = create_purchase_order({},'g')
    
    #Testing if anonymous user is trying to create or get the purchase orders
    assert response1.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To POST'
    assert response2.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To GET--ALL'
    assert response3.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To GET--ONE'


  def test_if_user_is_anonymous_and_accessing_vendor_returns_401(self,apiClient,vendor_set):
    response = apiClient.get(f'/api/purchase_orders?vendor_id={vendor_set.pk}/')
    
    #Testing if anonymous user is trying to get the purchase orders related to a vendor
    response.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To GET'
    
    
  def test_if_user_is_authenticated_and_accessing_vendor_returns_200(self,authenticate,apiClient,vendor_set):
    authenticate() #Used To Authenticate User -> Defined in conftest.py file
    
    response = apiClient.get(f'/api/purchase_orders?vendor_id={vendor_set.pk}/')
    
    #Testing if authenticated user is trying to get the purchase orders related to a vendor
    response.status_code == status.HTTP_200_OK,'User Should Access Vendor'
  
  
  def test_if_user_is_authenticated_and_data_is_invalid_returns_400(self,authenticate,create_purchase_order):
    authenticate() 
    
    response = create_purchase_order(
      {'po_number':'','delivery_date':'','quantity':'','issue_date':''}
      )
    
    #Testing if user posted data is invalid and the error is present or not
    assert response.status_code == status.HTTP_400_BAD_REQUEST,'Order Object Must Be Invalid'
    assert response.data['po_number'] is not None
    assert response.data['delivery_date'] is not None
    assert response.data['quantity'] is not None
    assert response.data['issue_date'] is not None
    
    
  def test_if_user_is_authenticated_and_data_is_valid_returns_200(self,authenticate,create_purchase_order,vendor_set):
    authenticate()

    response = create_purchase_order(
            {
              "po_number":"2",
              "items" : json.dumps([{'s': 1}]),
              "quantity":4,
              "vendor":vendor_set.pk,
              "delivery_date":datetime.datetime(2023, 12, 23, 4, 15, 0).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "status":"CM",
              "issue_date":datetime.datetime(2023, 6, 23, 11, 10, 0).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "order_date":datetime.datetime(2023, 6, 23, 5, 12, 0).strftime("%Y-%m-%dT%H:%M:%SZ")
            })
    
    #Testing if user posted data is valid and the po_number is present to make sure its created
    assert response.status_code == status.HTTP_201_CREATED,'Order Object Must Be Created'
    assert response.data['po_number'] is not None
    
    
  def test_if_user_is_authenticated_and_update_data_is_valid_returns_200(self,authenticate,create_purchase_order,vendor_set):
    authenticate()
    
    response = create_purchase_order(
            {
              "po_number":"2",
              "items" : json.dumps([{'s': 1}]),
              "quantity":5,
              "vendor":vendor_set.pk,
              "delivery_date":datetime.datetime(2023, 12, 23, 4, 15, 0).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "status":"CM",
              "issue_date":datetime.datetime(2023, 6, 23, 11, 10, 0).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "order_date":datetime.datetime(2023, 6, 23, 5, 12, 0).strftime("%Y-%m-%dT%H:%M:%SZ")
             }
      ,'p'
    )
    
    #Testing if data is updated correctly and the quantity is replaced
    assert response.status_code == status.HTTP_200_OK,'Order Object Must Be Updated'
    assert response.data['quantity'] == 5
    
    
  def test_if_user_is_authenticated_and_delete_data_is_valid_returns_200(self,authenticate,create_purchase_order):
    authenticate()
    
    response = create_purchase_order({},'d')
    
    #Testing if data is deleted
    assert response.status_code == status.HTTP_204_NO_CONTENT,'Order Object Must Be Deleted'
    
    
    
#This function returns endpoints based on the http method
@pytest.fixture
def create_acknowledge_date(apiClient,purchase_order_set):
  def do_create_acknowledge_date(acknowledge_date,method=None):
    purchase = purchase_order_set
    if method == 'g':
      return apiClient.get(f'/api/purchase_orders/{purchase.pk}/acknowledge/',acknowledge_date)
    else:
      return apiClient.post(f'/api/purchase_orders/{purchase.pk}/acknowledge/',acknowledge_date)
  return do_create_acknowledge_date
    
    
@pytest.mark.django_db
class TestAcknowledgePurchaseOrder:
  def test_if_user_is_anonymous_returns_401(self,create_acknowledge_date):
    response1 = create_acknowledge_date({'acknowledgment_date':''})
    response2 = create_acknowledge_date({},'g')
    
    #Testing if anonymous user is trying to create or get the acknowledgment_date
    assert response1.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To POST'
    assert response2.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To GET'
    
    
  def test_if_user_is_authenticated_and_data_is_valid_returns_201(self,authenticate,create_acknowledge_date):
    authenticate()    
    
    response = create_acknowledge_date(
                  {
                    'acknowledgment_date':datetime.datetime(2023, 7, 23, 21, 5, 0).strftime("%Y-%m-%dT%H:%M:%SZ")
                  }
                )
    
    #Testing if user posted data is valid and po_number is present
    assert response.status_code == status.HTTP_201_CREATED,'Acknowledgement Date Must Be Created'
    assert response.data['po_number'] is not None
    
    
  def test_if_user_is_authenticated_and_data_is_invalid_returns_400(self,authenticate,create_acknowledge_date):
    authenticate()    
    
    response = create_acknowledge_date({'acknowledgment_date':''})
    
    #Testing if user posted data is invalid and the error is present or not
    assert response.status_code == status.HTTP_400_BAD_REQUEST,'Acknowledgement Date Must Be Invalid'
    assert response.data['acknowledgment_date'] is not None