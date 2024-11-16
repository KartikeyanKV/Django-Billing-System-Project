from django.db import models
from Inventory.models import *

class Customer(models.Model):
    customer_name = models.CharField(max_length=200,null=True)
    customer_date = models.DateField(null=True)
    
    
    def __str__(self):
        return self.customer_name
    
    
    
class Order(models.Model):
    Product_reference = models.ForeignKey(Products,on_delete=models.SET_NULL, null=True)
    customer_reference = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    order_number = models.IntegerField(default=0)
    order_date = models.DateField(null=True)
    quantity = models.IntegerField(default=0)
    amount =  models.FloatField(default=0)  
    gst =  models.FloatField(default=0)  
    bill_amount =  models.FloatField(default=0)  
    
    
    def __str__(self):
        return self.order_name 
