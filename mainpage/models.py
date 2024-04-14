
#from turtle import title
from django.db import models
#from django.contrib.auth.models import User
from authentication.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField




class SlideShowM(models.Model):
	poster_name =models.CharField(max_length=255, blank=False)
	slides1 = models.ImageField(upload_to='Images/slideDisplay/', blank=True)
	slides2 = models.ImageField(upload_to='Images/slideDisplay/', blank=True)
	slides3 = models.ImageField(upload_to='Images/slideDisplay/', blank=True)
	Policy = models.TextField(blank=True)
	about_us = models.TextField(blank=True)
	terms_condtions = models.TextField(blank=True)

	class Meta:
		verbose_name_plural = 'slideshowms'

	def __str__(self):
		return self.poster_name

	def get_absolute_url(self):
		return reverse('mainpage:slideshow_list', args=[self.slug])	
	


class ServiceCategory(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)
	
	class Meta:
		verbose_name_plural = 'serviceCategories'

	def __str__(self):
		return self.name
    # it help us to dynamicly link to our service categories from the html
	def get_absolute_url(self):
		return reverse('mainpage:serviceCategory_list', args=[self.slug])


class Service(models.Model):
	sercategory = models.ForeignKey(ServiceCategory, related_name='service', on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	description1 = models.TextField(blank=True)
	description2 = models.TextField(blank=True)
	description3 = models.TextField(blank=True)
	description4 = models.TextField(blank=True)
	slug = models.SlugField(max_length=255)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	icon = models.ImageField(upload_to='Images/services/icon/', default='Images/default.jpg')
	image = models.ImageField(upload_to='Images/services', default='Images/default.jpg')
	is_active= models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'services'

	def get_absolute_url(self):
		return reverse('mainpage:service_detail', args=[self.slug])

	def __str__(self):
		return self.title


class HomeImage(models.Model):
	title = models.ForeignKey(ServiceCategory, related_name='homepageService', on_delete=models.CASCADE)
	service = models.ImageField(upload_to='Images/home_image/', blank=True)
	disciption = models.TextField(blank=True)

	class Meta:
		verbose_name_plural = 'homeimages'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('mainpage:home_images', args=[self.slug])		



class Contact(models.Model):
	username = models.CharField(max_length=255, blank=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	email = models.EmailField( max_length=255)
	subject = models.CharField(max_length=255)
	phone_number = PhoneNumberField()
	subject_description = models.TextField(blank=True)


	def __str__(self):
		return self.username