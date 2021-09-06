from django.db import models

# Create your models here.
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