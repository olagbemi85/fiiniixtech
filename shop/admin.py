from django.contrib import admin

from .models import *

@admin.register(Category)
class CatergoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductOwnCompany)
class ProductOwnCompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_email']
    #prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_type', 'model', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'model': ('capacity',)}    