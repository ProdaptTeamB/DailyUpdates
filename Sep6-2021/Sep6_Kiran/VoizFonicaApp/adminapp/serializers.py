from rest_framework import serializers
from adminapp.models import Query
class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Query
        fields=('id','name','phone_no','email_id','date','selectquery','message')