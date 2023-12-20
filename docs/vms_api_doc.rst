API Documentation
=================

User Management
--------------------------------------
1.  Registering a new user
    Endpoint: POST /auth/users/
    Description: Register a new user
    Request:
      Method: POST
      Body:
          {
            "username": "your_un",
            "password": "your_pw"
          }
    Response:
      Status Code: 201 Created
      Body:
          {
            "id": 1,
            "username":"your_un"
          }
2.  Listing all users
    Endpoint: GET /auth/users/
    Description: Only list all users if admin else it list only current user.
    Request:
      Method: GET
    Response:
      Status Code: 200 OK
      Body:
          [
            {
              "id": 1,
              "username": "your_un"
            }, -- if just a user the current users record will retrieve
            {
              "id": 2,
              "username": "your_un2"
            } 
            ... if admin will retrieve all users
          ]
3.  Retrieve auth_token owned user details
    Endpoint: GET /auth/users/me/
    Description: Retrieve auth_token owned user details.
    Request:
      Method: GET
    Response:
      Status Code: 200 OK
      Body:
          {
            "id": 1,
            "username": "your_un"
          }
            

Token Management
----------------
1.  Getting a new auth_token
    Endpoint: POST /auth/token/login/
    Description: Will get a new auth_token if posted login_details are correct
    Request:
      Method: POST
      Body: 
          {
            "username": "your_un",
            "password": "your_pw"
          }
    Response:
      Status Code: 200 OK
      Body: 
          {
            "auth_token": "s56gfgfdgdfdfsdw3434wewsdsds"
          }
2.  Removing a auth_token
    Headers: Set auth_token
    Endpoint: POST /auth/token/logout/
    Description: Destroys current auth_token
    Request:
      Method: POST
    Response:
      Status Code: 204 No Content


Vendor Profile Management
-------------------------
1.  Create a new vendor
    Headers: Set auth_token
    Endpoint: POST /api/vendors/
    Description: Create a new vendor profile.
    Request:
      Method: POST
      Body:
          {
            "name": "Alex",
            "contact_details": "9675645443",
            "address": "Gimy,New York,5466",
            "vendor_code": "456H",
          }
    Response:
      Status Code: 201 Created
      Body:
          {
            "id": 1,
            "name": "Alex",
            "contact_details": "9675645443",
            "address": "Gimy,New York,5466",
            "vendor_code": "456H",
            "on_time_delivery_rate": 0.0,
            "quality_rating_avg": 0.0,
            "average_response_time": 0.0,
            "fulfillment_rate": 0.0
          }
2.  List all vendors
    Headers: Set auth_token
    Endpoint: GET /api/vendors/
    Description: Retrieve a list of all vendors.
    Request:
      Method: GET
    Response:
      Status Code: 200 OK
      Body:
          [
            {
              "id": 1,
              "name": "Alex",
              "contact_details": "9675645443",
              "address": "Gimy,New York,5466",
              "vendor_code": "456H",
              "on_time_delivery_rate": 80.0,
              "quality_rating_avg": 4.5,
              "average_response_time": 2.5,
              "fulfillment_rate": 95.0
            },

          ]
3.  Retrieve a specific vendor's details
    Headers: Set auth_token
    Endpoint: GET /api/vendors/{vendor_id}/
    Description: Retrieve details of a specific vendor.
    Request:
      Method: GET
    Response:
      Status Code: 200 OK
      Body:
          {
            "id": 1,
            "name": "Alex",
            "contact_details": "9675645443",
            "address": "Gimy,New York,5466",
            "vendor_code": "456H",
            "on_time_delivery_rate": 80.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 2.5,
            "fulfillment_rate": 95.0
          }
4.  Update a vendor's details
    Headers: Set auth_token
    Endpoint: PUT /api/vendors/{vendor_id}/
    Description: Update a specific vendor's details.
    Request:
      Method: PUT
      Body:
          {
            "name": "Mathew",
            "contact_details": "9675645443",
            "address": "Gimy,New York,5466",
            "vendor_code": "456H",
          }
    Response:
      Status Code: 200 OK
      Body:
          {
            "id": 1,
            "name": "Mathew",
            "contact_details": "9675645443",
            "address": "Gimy,New York,5466",
            "vendor_code": "456H",
            "on_time_delivery_rate": 80.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 2.5,
            "fulfillment_rate": 95.0
          }
5.  Partial Update a vendor's details
    Headers: Set auth_token
    Endpoint: PATCH /api/vendors/{vendor_id}/
    Description: Update a specific part of vendor's details.
    Request:
      Method: PATCH
      Body:
          {
            "name": "Mathew22",
          }
    Response:
      Status Code: 200 OK
      Body:
          {
            "id": 1,
            "name": "Mathew22",
            "contact_details": "9675645443",
            "address": "Gimy,New York,5466",
            "vendor_code": "456H",
            "on_time_delivery_rate": 80.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 2.5,
            "fulfillment_rate": 95.0
          }
6.  Delete a vendor
    Headers: Set auth_token
    Endpoint: DELETE /api/vendors/{vendor_id}/
    Description: Delete a specific vendor.
    Request:
      Method: DELETE
    Response:
      Status Code: 204 No Content


Purchase Order Tracking
------------------------
1.  Create a new purchase order
    Headers: Set auth_token
    Endpoint: POST /api/purchase_orders/
    Description: Create a new purchase order.
    Request:
      Method: POST
      Body:
          {
            "po_number": "346HVfd",
            "vendor": 1,
            "order_date": "2023-12-01T12:00:00Z",
            "delivery_date": "2023-12-15T12:00:00Z",
            "items": {"tshirt": "5 Sleeve", "shirt": "Full Sleeve"},
            "quantity": 100,
            "status": "PN",
            "issue_date": "2023-12-01T12:00:00Z",
          }
    Response:
      Status Code: 201 Created
      Body:
          {
            "id": 1,
            "po_number": "346HVfd",
            "vendor": 1,
            "order_date": "2023-12-01T12:00:00Z",
            "delivery_date": "2023-12-15T12:00:00Z",
            "items": {"tshirt": "5 Sleeve", "shirt": "Full Sleeve"},
            "quantity": 100,
            "status": "PN",
            "quality_rating": null,
            "issue_date": "2023-12-01T12:00:00Z",
            "acknowledgment_date": null,
          }
2.  List all purchase orders
    Headers: Set auth_token
    Endpoint: GET /api/purchase_orders/
    Description: Retrieve a list of all purchase orders with an option to filter by vendor.
    Request:
      Method: GET
    Response:
      Status Code: 200 OK
      Body:
          [
            {
              "id": 1,
              "po_number": "346HVfd",
              "vendor": 1,
              "order_date": "2023-12-01T12:00:00Z",
              "delivery_date": "2023-12-15T12:00:00Z",
              "items": {"tshirt": "5 Sleeve", "shirt": "Full Sleeve"},
              "quantity": 100,
              "status": "PN",
              "quality_rating": null,
              "issue_date": "2023-12-01T12:00:00Z",
              "acknowledgment_date": null,
            },
            {
              "id":2,
              ........
            },
            ......
          ]
3.  Retrieve details of a specific purchase order
    Headers: Set auth_token
    Endpoint: GET /api/purchase_orders/{po_id}/
    Description: Retrieve details of a specific purchase order.
    Request:
      Method: GET
    Response:
      Status Code: 200 OK
      Body:
          {
            "id": 1,
            "po_number": "346HVfd",
            "vendor": 1,
            "order_date": "2023-12-01T12:00:00Z",
            "delivery_date": "2023-12-15T12:00:00Z",
            "items": {"tshirt": "5 Sleeve", "shirt": "Full Sleeve"},
            "quantity": 100,
            "status": "PN",
            "quality_rating": null,
            "issue_date": "2023-12-01T12:00:00Z",
            "acknowledgment_date": null,
          }

4.  Retrieve purchase order's related vendor.
    Headers: Set auth_token
    Endpoint : GET /api/purchase_orders/?vendor_id={vendor_id}
    Description : Retrieve all purchase orders of a specific vendor.
    Request:
      Method: GET
    Response:
      Status Code: 200 OK
      Body:
          [
            {
              "id": 1,
              "po_number": "346HVfd",
              "vendor": 1,
              "order_date": "2023-12-01T12:00:00Z",
              "delivery_date": "2023-12-15T12:00:00Z",
              "items": {"tshirt": "5 Sleeve", "shirt": "Full Sleeve"},
              "quantity": 100,
              "status": "CM",
              "quality_rating": 4.5
              "issue_date": "2023-12-01T12:00:00Z",
              "acknowledgment_date": null,
            },
            {
              "id":2,
              ........
            }
            .........
          ]
5.  Update a purchase order
    Headers: Set auth_token
    Endpoint: PUT /api/purchase_orders/{po_id}/
    Description: Update details of a specific purchase order.
    Request:
      Method: PUT
      Body:
          {
            "id": 1,
            "po_number": "346HVfd",
            "vendor": 1,
            "order_date": "2023-12-01T12:00:00Z",
            "delivery_date": "2023-12-15T12:00:00Z",
            "items": {"tshirt": "5 Sleeve", "shirt": "Full Sleeve"},
            "quantity": 100,
            "status": "CM",
            "quality_rating": 5.5
            "issue_date": "2023-12-01T12:00:00Z",
          }
    Response:
      Status Code: 200 OK
      Body:
          {
            "id": 1,
            "po_number": "346HVfd",
            "vendor": 1,
            "order_date": "2023-12-01T12:00:00Z",
            "delivery_date": "2023-12-15T12:00:00Z",
            "items": {"tshirt": "5 Sleeve", "shirt": "Full Sleeve"},
            "quantity": 100,
            "status": "CM",
            "quality_rating": 5.5
            "issue_date": "2023-12-01T12:00:00Z",
            "acknowledgment_date": null,
          }
6.  Partial Update a purchase order
    Headers: Set auth_token
    Endpoint: PATCH /api/purchase_orders/{po_id}/
    Description: Update a part of a specific purchase order.
    Request:
      Method: PATCH
      Body:
          {
            "status": "CM",
            "quality_rating": 4.5
          }
    Response:
      Status Code: 200 OK
      Body:
          {
            "id": 1,
            "po_number": "346HVfd",
            "vendor": 1,
            "order_date": "2023-12-01T12:00:00Z",
            "delivery_date": "2023-12-15T12:00:00Z",
            "items": {"tshirt": "5 Sleeve", "shirt": "Full Sleeve"},
            "quantity": 100,
            "status": "CM",
            "quality_rating": 4.5
            "issue_date": "2023-12-01T12:00:00Z",
            "acknowledgment_date": null,
          }
7.  Delete a purchase order
    Headers: Set auth_token
    Endpoint: DELETE /api/purchase_orders/{po_id}/
    Description: Delete a specific purchase order.
    Request:
      Method: DELETE
    Response:
      Status Code: 204 No Content


Vendor Performance Evaluation
------------------------------
1.  Retrieve a vendor's performance metrics
    Headers: Set auth_token
    Endpoint: GET /api/vendors/{vendor_id}/performance/
    Description: Retrieve performance metrics for a specific vendor.
    Request:
      Method: GET
    Response:
      Status Code: 200 OK
      Body:
          {
            "vendor": "123",
            "date": "2023-12-20T12:00:00Z"
            "on_time_delivery_rate": 80.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 2.5,
            "fulfillment_rate": 95.0
          }
2.  Create a new vendor's performance metrics
    Headers: Set auth_token
    Endpoint: POST /api/vendors/{vendor_id}/performance/
    Description: Create a new performance metrics for a specific vendor.
    Request:
      Method: POST
      Body: 
          {
            "date": "2023-12-20T12:00:00Z"
          }
    Response:
      Status Code: 201 Created
      Body:
          {
            "vendor": "123",
            "date": "2023-12-20T12:00:00Z"
            "on_time_delivery_rate": 80.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 2.5,
            "fulfillment_rate": 95.0
          }
3.  Delete a vendor's performance metrics
    Headers: Set auth_token
    Endpoint: DELETE /api/vendors/{vendor_id}/performance/{performance_id}/
    Description: Delete a performance metrics for a specific vendor.
    Request:
      Method: DELETE
    Response:
      Status Code: 204 No Content


Update Acknowledgment Endpoint
------------------------------
1.  Acknowledge a purchase order
    Headers: Set auth_token
    Endpoint: POST /api/purchase_orders/{po_id}/acknowledge/
    Description: Acknowledge a purchase order and update acknowledgment date.
    Request:
      Method: POST
      Body: 
          {
            "acknowledgment_date": "2023-12-01T12:00:00Z",
          }
    Response:
      Status Code: 200 OK 
      Body: 
          {
            "id": 1,
            "po_number": "346HVfd",
            "vendor": 1,
            "order_date": "2023-12-01T12:00:00Z",
            "actual_delivery_date": "2023-12-13T12:00:00Z",
            "expected_delivery_date": "2023-12-15T12:00:00Z",
            "items": {"tshirt": "5 Sleeve", "shirt": "Full Sleeve"},
            "quantity": 100,
            "status": "CM",
            "quality_rating": 4.5
            "issue_date": "2023-12-01T12:00:00Z",
            "acknowledgment_date": "2023-12-01T14:00:00Z",
          }

        
