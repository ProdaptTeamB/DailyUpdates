
#Employee

from rest_framework import serializers
from Admin.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('id','empcode','name','address','emailid','phonenumber','pincode','username','password','gender','aadhaarno','salary','dateofbirth','dateofjoining')



#Query

from rest_framework import serializers
from Admin.models import Query
class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Query
        fields=('id','name','phone_no','email_id','date','selectquery','message')


#Customer

from rest_framework import serializers
from Admin.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('id','DOB','username','password','product_type','purchase_date','name','gender','address','pincode','mobileno','email','adharno')






