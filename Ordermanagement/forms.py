from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Product_reference','customer_reference','order_number','order_date','quantity']
        
        

