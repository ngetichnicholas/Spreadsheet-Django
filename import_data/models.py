from django.db import models
from django import forms 

# Create your models here.
class Employee(models.Model):    
    employee_code = models.CharField(max_length=10, default='')
    first_name = models.CharField(max_length=150,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=30,null=True)
    phone_no = models.CharField(max_length=12, default='',null=True)
    address = models.CharField(max_length=500, default='',null=True) 
    gender = models.CharField(max_length=10, default='',null=True)
 
    def __str__(self):
        return self.first_name
                 
    objects = models.Manager()
