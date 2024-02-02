from django.contrib import admin

from .models import *


# Register your models here.

@admin.register(ServiceCategory)
class ServiceCatergoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SlideShowM)
class SlideShowMAdmin(admin.ModelAdmin):
    list_display = ['poster_name', 'Policy', 'about_us', 'terms_condtions', 'slides1', 'slides2', 'slides3']
    prepopulated_fields = {'Policy': ['Policy'], 'about_us': ['about_us'], 'terms_condtions': ['terms_condtions']}
    list_editable = ['Policy', 'about_us', 'terms_condtions', 'slides1', 'slides2', 'slides3']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']

"""
@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['phone_number'] 


@admin.register(UserProfileInfo)
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['address'] """

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name']    
  