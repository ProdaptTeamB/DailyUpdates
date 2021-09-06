from django.db import models

# Create your models here.
class Employee(models.Model):
    empcode=models.CharField(max_length=50)
    name=models.CharField(max_length=50,default='NO NAME',blank=True)
    address=models.CharField(max_length=50,default='NO NAME',blank=True)
    emailid=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50,default='NO NAME',blank=True)
    gender=models.CharField(max_length=50,default='NO NAME',blank=True)
    pincode=models.CharField(max_length=50,default='NO NAME',blank=True)
    aadhaarno=models.CharField(max_length=50,default='NO NAME',blank=True)
    dateofjoining=models.DateField()
    dateofbirth=models.DateField()
    salary=models.CharField(max_length=50,default='NO NAME',blank=True)
    username=models.CharField(max_length=50,default='NO NAME',blank=True)
    password=models.CharField(max_length=50,default='NO NAME',blank=True)