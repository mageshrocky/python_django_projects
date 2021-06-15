from uuid import uuid4

from django import forms
from .models import Customer, Shop


class Vcustomer(forms.ModelForm):

    name = forms.CharField(max_length=50, required=True)
    mobile = forms.CharField(max_length=12, required=True)
    product_name = forms.CharField(max_length=50, required=True)
    order_date = forms.CharField(max_length=30, required=True)
    delivery_date = forms.CharField(max_length=30, required=True)

    class Meta:
        model = Customer
        fields = ['name', 'mobile', 'product_name', 'order_date', 'delivery_date']


class Vshop(forms.ModelForm):
    product = forms.CharField(max_length=50, required=True)

    class Meta:
        model = Shop
        fields = {'product'}
