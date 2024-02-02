from django.db import models


class DataSolar(models.Model):
	days = models.DateField()
	hourly = models.TimeField()
	voltage = models.FloatField()
	currents = models.FloatField()
	power = models.FloatField()
	temp = models.FloatField()
	intensity = models.FloatField()
	
	class Meta:
		get_latest_by = ['days', 'hourly', 'voltage', 'currents', 'power', 'temp', 'intensity']
    
