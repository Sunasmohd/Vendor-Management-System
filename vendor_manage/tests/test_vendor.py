import pytest
from rest_framework import status
from datetime import datetime
from vendor_manage.models import *


#This function returns endpoints based on the http method
@pytest.fixture
def create_vendor(apiClient,vendor_set):
  def db_create_vendor(vendor,method=None):
    if method == 'd':
      return apiClient.delete(f'/api/vendors/{vendor_set.pk}/')
    elif method == 'p':
      return apiClient.put(f'/api/vendors/{vendor_set.pk}/',vendor)
    elif method == 'ga':
      return apiClient.get(f'/api/vendors/')
    elif method == 'g':
      return apiClient.get(f'/api/vendors/{vendor_set.pk}/')
    else:
      return apiClient.post('/api/vendors/',vendor)
  return db_create_vendor



@pytest.mark.django_db
class TestVendor:
  def test_if_user_is_anonymous_returns_401(self,create_vendor):
    response1 = create_vendor({'name':'d','contact_details': 's','address':'ss','vendor_code':"33"})
    response2 = create_vendor({},'ga')
    response3 = create_vendor({},'g')

    #Testing if anonymous user is trying to create or get the vendors
    assert response1.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To POST'
    assert response2.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To GET--ALL'
    assert response3.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To GET--ONE'
    
    
  def test_if_user_is_authenticated_and_data_is_valid_returns_201(self,authenticate,create_vendor):
    authenticate() #Used To Authenticate User -> Defined in conftest.py file
    
    response = create_vendor({'name':'d','contact_details': 's','address':'ss','vendor_code':"33"})
    
    #Testing if user posted data is valid and the vendor_code is present to make sure its created.
    assert response.status_code == status.HTTP_201_CREATED,'Vendor Object Must Be Created'
    assert response.data['vendor_code'] is not None
    
    
  def test_if_user_is_authenticated_and_data_is_invalid_returns_400(self,authenticate,create_vendor):
    authenticate()
    
    response = create_vendor({'name':'','contact_details': '','address':'','vendor_code':''})
    
    #Testing if user posted data is invalid and the error is present or not
    assert response.status_code == status.HTTP_400_BAD_REQUEST,'Vendor Object Must Be Invalid'
    assert response.data['name'] is not None
    assert response.data['contact_details'] is not None
    assert response.data['address'] is not None
    assert response.data['vendor_code'] is not None


  def test_if_user_is_authenticated_and_update_data_is_valid_returns_200(self,authenticate,create_vendor):
    authenticate()
    
    response = create_vendor(
                             {'name':'dd','contact_details': 's','address':'ss','vendor_code':"1234"},
                             'p'
                             )
    
    #Testing if data is updated correctly and the name is replaced
    assert response.status_code == status.HTTP_200_OK,'Vendor Object Must Be Updated'
    assert response.data['name'] == 'dd'

    
    
  def test_if_user_is_authenticated_and_delete_data_is_valid_returns_204(self,authenticate,create_vendor):
    authenticate()
    
    response = create_vendor({},'d')
    
    #Testing if data is deleted
    assert response.status_code == status.HTTP_204_NO_CONTENT,'Vendor Object Must Be Deleted'



#This function returns endpoints based on the http method
@pytest.fixture
def create_vendor_performance(apiClient,vendor_set,performance_set):
  def do_create_vendor_performance(performance_obj,method=None):
    vendor = vendor_set
    if method == 'p':
      return apiClient.put(f'/api/vendors/{vendor.pk}/performance/{performance_set.pk}/',performance_obj)
    elif method == 'd':
      return apiClient.delete(f'/api/vendors/{vendor.pk}/performance/{performance_set.pk}/')
    elif method == 'ga':
      return apiClient.get(f'/api/vendors/{vendor.pk}/performance/')
    elif method == 'g':
      return apiClient.get(f'/api/vendors/{vendor.pk}/performance/{performance_set.pk}/')
    else:
      return apiClient.post(f'/api/vendors/{vendor.pk}/performance/',performance_obj)
  return do_create_vendor_performance



@pytest.mark.django_db    
class TestVendorHistoricalPerformance:
  def test_if_user_is_anonymous_returns_401(self,create_vendor_performance):
    response1 = create_vendor_performance({'date':''})
    response2 = create_vendor_performance({},'ga')
    response3 = create_vendor_performance({},'g')
    
    #Testing if anonymous user is trying to create or get the historical performance
    assert response1.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To POST'
    assert response2.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To GET--ALL'
    assert response3.status_code == status.HTTP_401_UNAUTHORIZED,'User Not Allowed To GET--ONE'
    
    
  def test_if_user_is_authenticated_and_data_is_valid_returns_200(self,authenticate,create_vendor_performance):
    authenticate()
    
    response = create_vendor_performance(
                              {'date':datetime(2023, 12, 23, 21, 5, 0)}
                              )
    
    #Testing if user posted data is valid and the id > 0 to make sure its created.
    assert response.status_code == status.HTTP_201_CREATED,'Historical-Performance Object Must Be Created'
    assert response.data['id'] > 0
  

  def test_if_user_is_authenticated_and_data_is_invalid_returns_400(self,authenticate,create_vendor_performance):
    authenticate()
    
    response = create_vendor_performance(
                              {'date':''}
                              )
    
    #Testing if user posted data is invalid and the error is present or not
    assert response.status_code == status.HTTP_400_BAD_REQUEST,'Historical-Performance Object Must Be Invalid'
    
    
  def test_if_user_is_authenticated_and_delete_data_is_valid_returns_204(self,create_vendor_performance,authenticate):
    authenticate()
    
    response = create_vendor_performance({},'d')
    
    #Testing if data is deleted
    response.status_code == status.HTTP_204_NO_CONTENT,'Historical-Performance Object Must Be Deleted'
    
  
    
    
  
  

    