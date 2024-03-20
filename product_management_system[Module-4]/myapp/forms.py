
from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = product_mst
        fields = '__all__'

class ProductSubCatForm(forms.ModelForm):
    class Meta:
        model = product_sub_cat
        fields = '__all__'
