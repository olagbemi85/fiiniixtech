

from django import forms
from django.forms import ModelForm, widgets
from django.forms.widgets import NumberInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
#from location.models  import Country, State
from django_countries.widgets import CountrySelectWidget
#from image_uploader_widget.widgets import ImageUploaderWidget


class UserForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'username', 'type':'text'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'first name', 'type':'text'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'last name', 'type':'text'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs ={'class':'form-control' ,'placeholder':'password', 'type':'password'}))
    class Meta():
        model = User
        fields = ('username','password','email','first_name','last_name')


class UserFormUpdate(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'username', 'type':'text'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'first name', 'type':'text'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'last name', 'type':'text'}))
    #email = forms.EmailField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'email'}))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'address', 'type':'text'}))
    middle_name = forms.CharField(required=False, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'last name', 'type':'text'}))
    #country = forms.ModelChoiceField(required=False, queryset=Country.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    country = CountryField(blank_label="(select country)")
    #town_city = forms.ModelChoiceField(required=False, queryset=State.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    town_city = forms.CharField(required=False, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'last name', 'type':'text'}))
    phone_number = PhoneNumberField(required=False, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'phone'}))
    date_of_birth = forms.DateField(required=False, widget=NumberInput(attrs={'type': 'date', 'class':'form-control'}))
    profile_pic = forms.ImageField(required=False,
        widget = forms.FileInput(
            attrs = {"id" : "imgInp" , # you can access your image field with this id for css styling . 
                'style' : "max-height: 100px ; max-width : 100px ; ", # add style from here .
                "accept":"image/*", "type":"file"}))
    
    class Meta():
        model = User
        fields = ['username','first_name','last_name','middle_name', 'profile_pic','date_of_birth','phone_number','address','country','town_city']
        widgets = {"country": CountrySelectWidget()}               

'''
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfoAuth
        fields = ('address','phone_number','phone_number2','profile_pic')
        widgets = {
        		'address': forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'address'}),
        		#'profile_pic': forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'pic'}),
        		'phone_number': forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Phone Number'}),
        		'phone_number2': forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Phone Number'}),
        		}


class CustomerForm(forms.ModelForm):
	class Meta():
		model = CustomerUserAuth
		fields = ('phone_number', 'address')
		widgets = {
				 'phone_number': forms.TextInput(attrs ={'class' : 'form-control' ,'placeholder':'password'}),
				 'address': forms.TextInput(attrs ={'class' : 'form-control' ,'placeholder':'address'}),
				 }
'''    
     



