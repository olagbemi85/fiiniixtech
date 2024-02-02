from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','country','username','email']
    

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['stateName']
    
    
    


@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display =['localGovName']
        
    
       