from locust import HttpUser,task,between
import os
from django.core.wsgi import get_wsgi_application
from random import random
import math
import datetime
from decimal import Decimal
import json


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vendor_management_system.settings')

application = get_wsgi_application()

from vendor_manage.models import Vendor,Purchase,HistoricalPerformance


class Browse(HttpUser):
  
  wait_time = between(1,5)
  
  def on_start(self):
    if not hasattr(self,'auth_token') or not self.auth_token:
      self.login()
      
  
  def login(self): 
    data = {'username':'sunas','password':123}
    
    response = self.client.post(
      '/auth/token/login/',
      json=data,
      name='/login/'
    )
    
    assert response.status_code == 200, f'Login failed with status_code {response.status_code}'
    
    token = response.json()['auth_token']
    self.auth_token = {'Authorization':f'Token {token}'}
  
  
  ########## Vendors ###########
  
  
  @task(4)
  def view_vendors(self):
    headers = self.auth_token
    
    response = self.client.get('/api/vendors/',
                                name='/vendors',
                                headers=headers
                               )
  
    assert response.status_code == 200, f'Fetching Vendors failed with status_code {response.status_code}'
  
  
  @task(3)
  def view_vendor(self):
    vendor_count = Vendor.objects.count()
    random1 = math.floor(random() * vendor_count)
    
    if vendor_count > 0:
      vendor_id = Vendor.objects.values('vendor_code')[random1]['vendor_code']
      headers = self.auth_token
      
      response = self.client.get(
        f'/api/vendors/{vendor_id}/',
          name='/vendors/:id',
          headers=headers
      )
      
      assert response.status_code == 200, f'Fetching Vendor failed with status_code {response.status_code}'
    else:
      print('No vendor records exists')
 
 
  # This Test will cause many request so other request will be blocked because in this test
  # there is a while loop to test the existing vendor_code because it should be unique
    
  # @task(5)
  # def create_vendor(self):
  #   headers = self.auth_token
  #   vendor_code = None
      
  #   while vendor_code is None:
  #       random1 = math.floor(random() * 2000)
  #       response = self.client.get(f'/api/vendors/{random1}/',name='h',headers=headers)
  #       if response.status_code == 200:
  #         vendor_code = None
  #       else:
  #         vendor_code = str(random1)

  #   response = self.client.post(
  #     f'/api/vendors/',
  #     data={'name':'Joe',
  #           'contact_details': '21312322',
  #           'address':'Jim,New York,5656',
  #           'vendor_code':vendor_code
  #     },
  #     name='/vendors/create',
  #     headers=headers
  #   )
    
  #   assert response.status_code == 201, f'Creating Vendor failed with status_code {response.status_code}'
    
    
  @task(4)
  def update_vendors(self):
    vendor_count = Vendor.objects.count()
    random1 = math.floor(random() * vendor_count)
    
    if vendor_count > 0:
      vendor_id = Vendor.objects.values('vendor_code')[random1]['vendor_code']
      headers = self.auth_token
      
      response = self.client.put(f'/api/vendors/{vendor_id}/',
                                  name='/vendors/:id/update',
                                  data={
                                    'name':f'Joe{random1}',
                                    'contact_details': '21312322',
                                    'address':'Hey,India,5656',
                                    'vendor_code':str(vendor_id)
                                  },
                                  headers=headers
                                )  
      
      response.status_code == 200,f'Updating Vendors failed with status code {response.status_code}'
    else:
      print('No vendor records exists')
  
  
  # Deleting a vendor is rarely done
  
  # @task(1)
  # def delete_vendor(self):
  #   vendor_count = Vendor.objects.count()
  #   random1 = math.floor(random() * vendor_count)
  
  #   if vendor_count > 0:
  #     vendor_id = Vendor.objects.values('vendor_code')[random1]['vendor_code']
  #     headers = self.auth_token 

  #     response = self.client.delete(f'/api/vendors/{vendor_id}/',
  #                                     name='/vendors/:id/delete',
  #                                     headers=headers
  #                                   ),
      
  #     response[0].status_code == 204,f'Deleting Vendors fialed with status code {response[0].status_code}'
  #   else:
  #     print('No vendor records exists')
  
  
  ########## Purchase Orders ###########
    
    
  @task(6)
  def view_vendor_purchase_orders(self):
    vendor_count = Vendor.objects.count()
    random1 = math.floor(random() * vendor_count)
    
    if vendor_count > 0:
      vendor_id = Vendor.objects.values('vendor_code')[random1]['vendor_code']
      headers = self.auth_token
    
      response = self.client.get(
        f'/api/purchase_orders/?vendor_id={vendor_id}',
          name='/purchase_orders/?vendor_id:id',
          headers=headers
      )
      
      assert response.status_code == 200, f'Fetching Vendor Related Purchase Orders Vendor failed with status_code : {response.status_code}'
    else:
      print('No vendor records exists')
    
    
  @task(3)
  def view_purchase_orders(self):
    headers = self.auth_token
    
    response = self.client.get('/api/purchase_orders/',
                                name='/purchase_orders',
                                headers=headers
                              )
  
    assert response.status_code == 200, f'Fetching Purchase Orders failed with status_code {response.status_code}'
  

  @task(4)
  def view_purchase_order(self):
    po_count = Purchase.objects.count()
    random1 = math.floor(random() * po_count)
    
    if po_count > 0:
      purchase_id = Purchase.objects.values('po_number')[random1]['po_number']
      headers = self.auth_token
      
      response = self.client.get(
        f'/api/purchase_orders/{purchase_id}/',
          name='/purchase_orders/:id',
          headers=headers
      )
      
      assert response.status_code == 200, f'Fetching Purchase Orders failed with status_code {response.status_code}'
    else:
      print('No PO records exists')
    
    
  # This Testing will send many requests so other requests will be blocked because in this test
  # there is a while loop to test the existing po_number because it should be unique
  
  # @task(6)
  # def create_purchase_order(self):
  #   vendor_count = Vendor.objects.count()
  #   random1 = math.floor(random() * vendor_count)
  
  #   if vendor_count > 0:
  #     vendor_id = Vendor.objects.values('vendor_code')[random1]['vendor_code']
  #     headers = self.auth_token
  #     po_number = None
    
  #     while po_number is None:
  #         random2 = math.floor(random() * 2000)
  #         response = self.client.get(f'/api/purchase_orders/{random2}/',name='g',headers=headers)
  #         if response.status_code == 200:
  #           po_number = None
  #         else:
  #           po_number = str(random2)
    
  #     response = self.client.post(
  #       f'/api/purchase_orders/',
  #       data = {
  #               "po_number":po_number,
  #               "items" : json.dumps([{'s': 1}]),
  #               "quantity":4,
  #               "vendor":vendor_id,
  #               "delivery_date":datetime.datetime(2023, 12, 23, 4, 15, 0).strftime("%Y-%m-%dT%H:%M:%SZ"),
  #               "status":"PN",
  #               "issue_date":datetime.datetime(2023, 6, 23, 11, 10, 0).strftime("%Y-%m-%dT%H:%M:%SZ"),
  #               "order_date":datetime.datetime(2023, 6, 23, 5, 12, 0).strftime("%Y-%m-%dT%H:%M:%SZ")
  #             },
  #       name='/purchase_orders/create',
  #       headers=headers
  #     )
      
  #     assert response.status_code == 201, f'Creating Purchase Orders failed with status_code {response.status_code}'
  #   else:
  #     print('No vendor records exists')
    
    
  @task(4)
  def update_purchase_orders(self):
    vendor_count = Vendor.objects.count()  
    random1 = math.floor(random() * vendor_count)
    if vendor_count > 0:
      vendor_id = Vendor.objects.values('vendor_code')[random1]['vendor_code']
      po = Purchase.objects.filter(vendor_id=vendor_id)
      po_count = po.count()
      random2 = math.floor(random() * po_count)
    
      if po_count > 0:
        po_id = po.values('po_number')[random2]['po_number']
        
        headers = self.auth_token
        quality_rating = round(Decimal(random() * 10),1)
        
        response = self.client.patch(f'/api/purchase_orders/{po_id}/',
                                      name='/purchase_orders/:id/update',
                                      data = {
                                          "po_number":po_id,
                                          "items" : json.dumps([{'s': 1}]),
                                          "quantity":4,
                                          "vendor":vendor_id,
                                          "delivery_date":datetime.datetime(2023, 12, 23, 4, 15, 0).strftime("%Y-%m-%dT%H:%M:%SZ"),
                                          "status":"CM",
                                          "quality_rating":quality_rating,
                                          "issue_date":datetime.datetime(2023, 6, 23, 11, 10, 0).strftime("%Y-%m-%dT%H:%M:%SZ"),
                                          "order_date":datetime.datetime(2023, 6, 23, 5, 12, 0).strftime("%Y-%m-%dT%H:%M:%SZ")
                                      },
                                      headers=headers
                                    )
        
        response.status_code == 200,f'Updating Vendors failed with status code {response.status_code}'
      else:
        print('No PO records exists')
    else:
        print('No Vendor records exists')
  
  
  # Deleting a po is rarely done
  
  # @task(1)
  # def delete_purchase_order(self):
  #   po_count = Purchase.objects.count()
  #   random1 = math.floor(random() * po_count)
  
  #   if po_count > 0:
  #     po_id = Purchase.objects.values('po_number')[random1]['po_number']
  #     headers = self.auth_token
      
  #     response = self.client.delete(f'/api/purchase_orders/{po_id}/',
  #                                   name='/purchase_orders/:id/delete',
  #                                   headers=headers
  #                                   )
      
  #     assert response.status_code == 204,f'Deleting a purchase order failed with a status code {response.status_code}'
  #   else:
  #     print('No PO records exists')
  
  
  ########## Acknowledge Purchase Orders ###########
  
  
  @task(5)
  def acknowledge_order(self):
    po_count = Purchase.objects.count()
    random1 = math.floor(random() * po_count)
    
    if po_count > 0:
      purchase_id = Purchase.objects.values('po_number')[random1]['po_number']
      headers = self.auth_token
      
      response = self.client.post(
        f'/api/purchase_orders/{purchase_id}/acknowledge/',
        data={'acknowledgment_date':datetime.datetime(2023, 12, 11, 22, 2, 11)},
        name='/purchase_orders/:id/acknowledge',headers=headers
      )
      
      assert response.status_code == 201, f'Purchase Order Acknowledge failed with status_code {response.status_code}'
    else:
      print('No PO records exists')


  ########## Historical Performance ###########
  
  
  @task(2)
  def get_historical_performance(self):
    vendor_count = Vendor.objects.count()
    random1 = math.floor(random() * vendor_count)
    
    if vendor_count > 0:
      vendor_id = Vendor.objects.values('vendor_code')[random1]['vendor_code']
      headers = self.auth_token
      
      response = self.client.get(
        f'/api/vendors/{vendor_id}/performance/',
        name='/vendors/:id/performance',
        headers=headers
      )
      
      assert response.status_code == 200, f'Fetching Historical Response failed with status_code {response.status_code}'
    else:
      print('No vendor records exists')
    
    
  @task(2)
  def create_historical_performance(self):
    vendor_count = Vendor.objects.count()
    random1 = math.floor(random() * vendor_count)
    
    if vendor_count > 0:
      vendor_id = Vendor.objects.values('vendor_code')[random1]['vendor_code']
      headers = self.auth_token
      month = math.ceil(random() * 12)
      day = math.ceil(random() * 30)
      hour = math.ceil(random() * 23)
      minute = math.ceil(random() * 59)
      second = math.ceil(random() * 59)
      
      if month == 2 and day > 28:
        day = 28
        
      response = self.client.post(
        f'/api/vendors/{vendor_id}/performance/',
        data = {
          'date':datetime.datetime(2023, month, day, hour, minute, second)
        },
        name='/vendors/:id/performance/create',
        headers=headers
      )
      
      assert response.status_code == 201, f'Creating Historical Performance failed with status_code {response.status_code}'
    else:
        print('No vendor records exists')
    
    
  @task(4)
  def delete_historical_performance(self):
    vendor_count = Vendor.objects.count()
    random2 = math.floor(random() * vendor_count)
    if vendor_count > 0:
      vendor_id = Vendor.objects.values('vendor_code')[random2]['vendor_code']
      hp_count = HistoricalPerformance.objects.filter(vendor_id=vendor_id).count()
      random1 = math.floor(random() * hp_count)
    
      if hp_count > 0:
        hp_id = HistoricalPerformance.objects.filter(vendor_id=vendor_id).values('id')[random1]['id']
        headers = self.auth_token
        response = self.client.delete(f'/api/vendors/{vendor_id}/performance/{hp_id}/',
                                        name='/vendors/:id/performance/:id/delete',
                                        headers=headers
                                     )    
      
        assert response.status_code == 204,f'Deleting Historical Performance failed with status code {response.status_code}'
      else:
        print(f'No HP records exist for the vendor {vendor_id}')
    else:
      print('No vendor records exists')
      

  @task(1)
  def view_users(self):
    headers = self.auth_token
    
    response = self.client.get('/auth/users/me/',
                                name='/user',
                                headers=headers
                              )
    
    assert response.status_code == 200, f'Fetching User failed with status_code {response.status_code}'
