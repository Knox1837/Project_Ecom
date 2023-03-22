from django import forms
from .models import Product, Category
 
class ProductAddForm(forms.ModelForm):
    class Meta:
        #fields="__all__" for all fields
        fields=("title", "desc", "price", "category", "quantity", "discount", "cash_on_delivery") #for selective fields      
        model=Product
class CategoryAddForm(forms.ModelForm):
    class Meta:
        fields=('category_name',)
        model=Category