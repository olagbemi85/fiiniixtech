from django.contrib import admin
from .models import DataSolar




class dataSolarAdmin(admin.ModelAdmin):
	list_display=('voltage','currents','power','hourly', 'intensity', 'temp','days')
	#list_editable =['days','currents','power','hourly', 'intensity', 'temp']

admin.site.register(DataSolar, dataSolarAdmin)
