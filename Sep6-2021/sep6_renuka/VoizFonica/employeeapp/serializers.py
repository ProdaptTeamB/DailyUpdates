from rest_framework import serializers
from employeeapp.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('id','empcode','name','address','emailid','phonenumber','pincode','username','password','gender','aadhaarno','salary','dateofbirth','dateofjoining')