

from django import forms
from django.forms import ModelForm, widgets
from django.forms.widgets import NumberInput
from .models import *
from django_countries.widgets import CountrySelectWidget
from authentication.models import State, LGA
from authentication.models import User



class UserSPSForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'First Name', 'type':'text'}))
    company = forms.ModelChoiceField(required=False, queryset=Company.objects.all())
    staff_position = forms.ModelChoiceField(required=False, queryset=Position.objects.all())
    staff_level = forms.ModelChoiceField(required=False, queryset=Level.objects.all())
    staff_id_no = forms.IntegerField(required=True, widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'ID Number', 'type':'text'}))
    area_office = forms.ModelChoiceField(required=True, queryset=AreaOffice.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    regional_office = forms.ModelChoiceField(required=True, queryset=Region.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta():
        model = UserProfile
        fields = ('first_name','company','staff_position','staff_level','staff_id_no','area_office','regional_office')


'''
class StationForm(forms.ModelForm):
    user_profile = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
    company = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Company Name', 'type':'text'}))
    station_name = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Substation Name', 'type':'text'}))
    station_code = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Substation Code', 'type':'text'}))
    station_location = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Substation Code', 'type':'text'}))
    longtitudes = forms.FloatField(required=True, widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'site Longtitude', 'type':'text'}))
    latitude = forms.FloatField(required=True, widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'site Latitude', 'type':'text'}))
    #user_profile = forms.ModelMultipleChoiceField(required=True, queryset=UserProfile.objects.all(),  widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
    area_office = forms.ModelChoiceField(required=True, queryset=AreaOffice.objects.all(),  widget=forms.Select(attrs={'class': 'form-control show-tick'}))
    regional_office = forms.ModelChoiceField(required=True, queryset=Region.objects.all(),  widget=forms.Select(attrs={'class': 'form-control show-tick'}))
    country = CountryField(blank_label="(select country)")
    local_gov_area = forms.ModelChoiceField(required=False, queryset=LGA.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    state = forms.ModelChoiceField(required=False, queryset=State.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}))
    max_power = forms.FloatField(required=True, widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'Transformer Capacity (KW)', 'type':'text'}))
    zipcode = forms.IntegerField(required=True, widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'Substation Code', 'type':'text'}))
    
    class Meta():
        model = Station
        fields = ('user_profile','company','station_name','station_code','station_location','area_office','regional_office','latitude','longtitudes')
'''

class StationForm(forms.ModelForm):
    user_profile = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all())
    company = forms.ModelChoiceField(required=False, queryset=Company.objects.all())
    station_name = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Substation Name', 'type':'text'}))
    station_code = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Substation Code', 'type':'text'}))
    station_location = forms.CharField(required=True, widget=forms.TextInput(attrs ={'class':'form-control' ,'placeholder':'Substation Code', 'type':'text'}))
    longtitudes = forms.FloatField(required=True, widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'site Longtitude', 'type':'text'}))
    latitude = forms.FloatField(required=True, widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'site Latitude', 'type':'text'}))
    #user_profile = forms.ModelMultipleChoiceField(required=True, queryset=UserProfile.objects.all(),  widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
    area_office = forms.ModelChoiceField(required=True, queryset=AreaOffice.objects.all())
    regional_office = forms.ModelChoiceField(required=True, queryset=Region.objects.all())
    country = CountryField(blank_label="(select country)")
    local_gov_area = forms.ModelChoiceField(required=False, queryset=LGA.objects.all())
    state = forms.ModelChoiceField(required=False, queryset=State.objects.all())
    max_power = forms.FloatField(required=True, widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'Transformer Capacity (KW)', 'type':'text'}))
    zipcode = forms.IntegerField(required=True, widget=forms.NumberInput(attrs ={'class':'form-control' ,'placeholder':'Substation Code', 'type':'text'}))
    
    class Meta():
        model = Station
        fields = ('user_profile','company','station_name','station_code','station_location','area_office','regional_office','latitude','longtitudes','country','zipcode','max_power','state','local_gov_area')
    
