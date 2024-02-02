from django.contrib import admin
from .models import Data,UserProfile, Station,Region, AreaOffice,Company,Level,Position




class dataPowerAdmin(admin.ModelAdmin):
	list_display=('voltage_r', 'voltage_y', 'voltage_b', 'currents_r', 'currents_y', 'currents_b', 'power_r', 'power_y', 'power_b', 'temp', 'station_code', 'days','hourly')
admin.site.register(Data, dataPowerAdmin)


# Register your models here.
#@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('staff_id_no','user','company','regional_office','staff_id_no','staff_position','staff_level', 'area_office')
    list_editable =  ['regional_office','staff_position','staff_level']
    list_display_links = ("staff_id_no", )
admin.site.register(UserProfile, UserProfileAdmin)    


#@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    #list_display = ('station_name')
    list_display = ['station_name','company','regional_office','code','location','max_power', 'area_office','state','local_gov_area','latitude','longtitudes']    
admin.site.register(Station, StationAdmin)    


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_editable =  ['name']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_editable =  ['name']


@admin.register(AreaOffice)
class AreaOfficeAdmin(admin.ModelAdmin):
    list_display =['name','region']
    list_editable = ['region']
    list_display_links = ("name", )
 
 
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_editable =  ['name']
    

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_editable =  ['name']         