# Vendor Management System
A Vendor Management System build using Django and Django Rest Framework.This will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

# Setup Instructions
**Clone the repository**
```
git clone https://github.com/Sunasmohd/Vendor-Management-System.git
```
**Navigate to the project repository**
```
cd Vendor-Management-System
```
**Create a virtual environment**
```
virtualenv venv
```
**Activate the virtual environment**
```
venv\Scripts\activate
```
**Install dependencies**
```
pip install -r requirements.txt
```
**Apply database migrations**
```
python manage.py migrate
```
**Run the development server**
```
python manage.py runserver
```

# Configuration
**Setup your database**
* Create a database
* Add a .env file in your root directory and add your database details
```
DB_ENGINE=django.db.backends.mysql
DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost or your_public_db_host
DB_PORT=3306 or your_public_db_port
```
* After creating database
```
python manage.py migrate
```
* This will create the tables based on the models

**Getting the token**
* To access every endpoint you need an auth_token
* You need to register first
```
import requests

# Replace it with your original username and password
login_details = {'username':'your_username','password':'your_password'}
response = requests.post('http://127.0.0.1:8000/auth/users/',login_details)
data = response.json()

# You can confirm the creation of your account
if 'id' in data:
  print(data['id'])
# You can catch any validation errors and fix it
else:
  print(data) 
```
* You can create a superuser too
```
python manage.py createsuperuser
```
* Both will create a user record in the database
* Send your login details to get a token
* After getting the token add it to the headers of the request
```
import requests

# Replace it with your original username and password
login_details = {'username':'your_username','password':'your_password'}
response = requests.post('http://127.0.0.1:8000/auth/token/login/',login_details)
data = response.json()

# If no error occured it will successfully access all the vendors records
if 'auth_token' in data:
  headers = {'Authorization' : f'Token {data["auth_token"]}'}
  response = requests.get('http://127.0.0.1:8000/api/vendors/',headers=headers)
  data = response.json()

```

# API Usage
API Usage is briefly defined in [VMS API Documentation](https://github.com/Sunasmohd/Vendor-Management-System/blob/main/docs/vms_api_doc.rst).

# Running A Test Suite
**Run all tests in one go**
```
pytest
```
**Run a specific file**
* Navigate to the tests folder
```
cd vendor_manage\tests
```
* Choose one of the files
```
pytest test_vendor.py
```

# Running A Performance Test
* Run locust in a one terminal
```
locust -f locustfiles/browse_api.py
```
* Run server in other terminal
```
python manage.py runserver
```
* Locust will start running at
```
http://localhost:8089/
```
* Locust will access our database and directly make CRUD operations to it to test the real performance.
  
![Locust Screenshot 1](https://github.com/Sunasmohd/Vendor-Management-System/blob/main/assets/images/Locust1.PNG)
* Number of users = Total no of users browsing
* Spawn rate = New users per second
* Host = localhost or your public domain name
