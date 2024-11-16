from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        
        widgets = {
            "product_name": forms.TextInput(attrs={'class':'form-control'}),
            "product_id":forms.TextInput(attrs={'class':'form-control'}),
            "product_price":forms.NumberInput(attrs={'class':'form-control'}),
            "product_GST":forms.NumberInput(attrs={'class':'form-control'}),
            "picture":forms.FileInput(attrs={'class':'form-control'}),
        }
