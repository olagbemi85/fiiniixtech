from django.db import models
from authentication.models import User
from django.conf import settings
from django.urls import reverse
from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    company = models.CharField(max_length=255, null=True)
    regional_office =  models.CharField(max_length=255, null=True)
    staff_id_no =  models.IntegerField( null=True)
    area_office =  models.CharField(max_length=255, null=True)
    staff_level =  models.CharField(max_length=255, null=True)
    staff_position =  models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255)

    #def __str__(self):
    #    return '{} {} {} {} {} {} {}'.format(self.user,self.first_name,self.company,self.regional_office,self.staff_id_no,self.area_office,self.staff_position)
    
    def __str__(self):
        return self.first_name




class Station(models.Model):
    company = models.CharField(max_length=255)
    regional_office =  models.CharField(max_length=255)
    area_office =  models.CharField(max_length=255)
    station_name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    profile = models.ManyToManyField(UserProfile)
    location=  models.CharField(max_length=255)
    longtitudes = models.FloatField()
    latitude = models.FloatField()
    max_power = models.FloatField(max_length=255)
    zipcode = models.IntegerField(null=True)
    country = CountryField()
    local_gov_area = models.CharField(max_length=225, null=True)
    state = models.SlugField(max_length=225, null=False)

    def get_absolute_url(self):
        return reverse('smartpower:station_detail', args=[self.code])

    def __str__(self):
        return self.station_name
    
    

class Data(models.Model):
    days = models.DateField()
    hourly = models.TimeField()
    voltage_r = models.FloatField()
    voltage_y = models.FloatField()
    voltage_b = models.FloatField()
    currents_r = models.FloatField()
    currents_y = models.FloatField()
    currents_b = models.FloatField()
    power_r = models.FloatField()
    power_y = models.FloatField()
    power_b = models.FloatField()
    temp = models.FloatField()
    station_code = models.SlugField(max_length=255, null=False)

    class Meta:
        get_latest_by = ['days', 'hourly', 'voltage_r','voltage_y','voltage_b',
                    'currents_r','currents_y','currents_b',
                      'power_r','power_y','power_b',
                        'temp', 'station_code']
    
    
    #def get_absolute_url(self): 
    #    return reverse('smartpower:sps_data', args=[self.station_code])


class Company(models.Model):
    name = models.CharField(max_length=225)
    slug =  models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name


class Region(models.Model):
    company = models.ForeignKey(Company, related_name='region', on_delete=models.CASCADE)  
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, unique=True)  
    
    def __str__(self):
        return self.name
 
    
class AreaOffice(models.Model):
    region = models.ForeignKey(Region, related_name='area_office', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name    


class Level(models.Model):
    company = models.ForeignKey(Company, related_name='level', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
    
class Position(models.Model):
    Company = models.ForeignKey(Company, related_name='position', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name