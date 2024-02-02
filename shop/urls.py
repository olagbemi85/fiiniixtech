
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'shop'


urlpatterns = [
	path('product/', views.all_products, name='product'),
 	path('category/product/<slug:slug>/', views.category_list, name='category_list'),
 	path('all-product/product/<slug:slug>/', views.product_detail, name='product_detail'),
]
