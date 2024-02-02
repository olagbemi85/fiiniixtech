
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'mainpage'


urlpatterns = [
	path('', views.home, name='home'),
	path('contact_us', views.contact_us, name='contact_us'),
	path('fx_policy', views.all_slideshows, name='fx_policy'),
	path('about', views.slideshows_about, name='about'),
	path('terms', views.slideshows_terms, name='terms'),
	path('service/', views.all_service, name='all_service'),
	path('item/<slug:slug>/', views.service_detail, name='service_detail'),
    path('search/<slug:sercategory_slug>/', views.serviceCategory_list, name='serviceCategory_list'),
	#path('product/', views.all_products, name='product'),
 	#path('category/product/<slug:slug>/', views.category_list, name='category_list'),
 	#path('all-product/product/<slug:slug>/', views.product_detail, name='product_detail'),
]
