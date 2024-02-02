
#from turtle import title
from django.db import models
#from django.contrib.auth.models import User
from authentication.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


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
		return reverse('shop:category_list', args=[self.slug])


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
	image = models.ImageField(upload_to='shop/products/', default='Images/default.jpg')
	image2 = models.ImageField(upload_to='shop/products/', blank=True)
	image3 = models.ImageField(upload_to='shop/products/', blank=True)
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
		return reverse('shop:product_detail', args=[self.slug])


	def __str__(self):
		return self.title
