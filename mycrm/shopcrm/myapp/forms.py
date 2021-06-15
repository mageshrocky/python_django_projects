from django import forms
from datetime import date
from .models import Customer, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
