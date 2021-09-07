from django.db import models


#Employee 

class Employee(models.Model):
    empcode=models.CharField(max_length=50)
    name=models.CharField(max_length=50,default='NO NAME',blank=True)
    address=models.CharField(max_length=50,default='NO NAME',blank=True)
    emailid=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50,default='NO NAME',blank=True)
    gender=models.CharField(max_length=50,default='NO NAME',blank=True)
    pincode=models.CharField(max_length=50,default='NO NAME',blank=True)
    aadhaarno=models.CharField(max_length=50,default='NO NAME',blank=True)
    dateofjoining=models.CharField(max_length=50)
    dateofbirth=models.CharField(max_length=50)
    salary=models.CharField(max_length=50,default='NO NAME',blank=True)
    username=models.CharField(max_length=50,default='NO NAME',blank=True)
    password=models.CharField(max_length=50,default='NO NAME',blank=True)

    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)




# Query.
class Query(models.Model):
    name=models.CharField(max_length=50)
    phone_no=models.BigIntegerField()
    email_id=models.EmailField(max_length=100)
    date=models.CharField(max_length=100,default='',blank=True)
    selectquery=models.CharField(max_length=100)
    # feedback=models.CharField(max_length=500,default='',blank=True)
    # questions=models.CharField(max_length=500,default='',blank=True)
    # complaints=models.CharField(max_length=500,default='',blank=True)
    message=models.CharField(max_length=500,default='',blank=True)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)





# Customer

class Customer(models.Model):
    name=models.CharField(max_length=50)
    DOB=models.CharField(max_length=50)
    purchase_date=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    adharno=models.CharField(max_length=50)
    product_type=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)
