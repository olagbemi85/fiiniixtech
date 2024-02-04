

from django import forms
from django.forms import ModelForm, widgets
from django.forms.widgets import NumberInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django_countries.widgets import CountrySelectWidget



class SearchProductForm(forms.Form):
    product_type= forms.CharField(required=False, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'product name', 'type':'text'}))
    capacity = forms.CharField(required=False, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'capacity', 'type':'text'}))
    model = forms.CharField(required=False, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'last name', 'type':'text'}))
    name_of_manufaturer = forms.EmailField(required=False, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'email'}))
    
    class Meta():
        fields = ('product_type','capacity','model','name_of_manufaturer')


