from django import forms
from .models import Product
 
class ProductAddForm(forms.ModelForm):
    class Meta:
        #fields="__all__" for all fields
        fields=("title", "desc", "category", "price", "image", "quantity", "discount", "cash_on_delivery"), #for selective fields      
        model=Product
