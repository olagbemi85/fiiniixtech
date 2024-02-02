
#from turtle import title
from django.db import models
#from django.contrib.auth.models import User
from authentication.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

'''
class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)
	description = models.TextField(blank=True)


	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name
    # it help us to dynamicly link to our categories from the html
	def get_absolute_url(self):
		return reverse('mainpage:category_list', args=[self.slug])


class ProductManager(models.Manager):
	def get_queryset(self):
		return super(ProductManager, self).get_queryset().filter(is_active=True)

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
	created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
	product_type = models.CharField(max_length=255)
	model = models.CharField(max_length=255)
	capacity = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	name_of_manufaturer = models.CharField(max_length=255)
	Country_of_manufature = CountryField()
	year_of_production = models.DateTimeField()
	author = models.CharField(max_length=255, default='admin')
	description = models.TextField(blank=True)
	description2 = models.TextField(blank=True)
	image = models.ImageField(upload_to='mainpage/Images/products/', default='Images/default.jpg')
	image2 = models.ImageField(upload_to='mainpage/Images/products/', blank=True)
	image3 = models.ImageField(upload_to='mainpage/Images/products/', blank=True)
	slug = models.SlugField(max_length=255)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	#puchase_price = models.DecimalField(max_digits=12,  decimal_places=2)
	sell_price = models.DecimalField(max_digits=12,  decimal_places=2)
	in_stock = models.BooleanField(default=True)
	is_active= models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add= True)
	updated = models.DateTimeField(auto_now=True)
	objects = models.Manager()
	products = ProductManager()


	class Meta:
		verbose_name_plural = 'products'
		ordering = ('-created',)
       # it help us to dynamicly link to our categories from the html

	def get_absolute_url(self):
		return reverse('mainpage:product_detail', args=[self.slug])


	def __str__(self):
		return self.title       '''


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