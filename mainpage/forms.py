from django.forms import ModelForm, widgets
from django import forms
from .models import *
from django.contrib.auth.models import User


'''
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ('username','password','email','first_name','last_name')
		widgets = {
				 'username': forms.TextInput(attrs ={'class' : 'form-control' ,'placeholder':'username'}),
				 'first_name': forms.TextInput(attrs ={'class' : 'form-control' ,'placeholder':'firstname'}),
				 'last_name': forms.TextInput(attrs ={'class' : 'form-control' ,'placeholder':'lastname'}),
				 'password': forms.TextInput(attrs ={'class' : 'form-control' ,'placeholder':'password'}),
				 'email': forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'email'}),
				 }


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('address','profile_pic')
        widgets = {
        		'address': forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'address'}),
        		}


class CustomerForm(forms.ModelForm):
	class Meta():
		model = CustomerUser
		fields = ('phone_number', 'address')
		widgets = {
				 'phone_number': forms.TextInput(attrs ={'class' : 'form-control' ,'placeholder':'password'}),
				 'address': forms.TextInput(attrs ={'class' : 'form-control' ,'placeholder':'address'}),
				 }




	SUBJECT_CHOICES=(
		(1, "Enquiry"),
		(2, "Complain"),
		(3, "Appreciate")
	)
'''