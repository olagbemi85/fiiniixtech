from urllib import request
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import *
from django.http import JsonResponse
import datetime
from iotSolar_proj.serializers import SolarDataSerializer
from django.core import serializers

from django.views.generic.list import ListView
from django.utils import timezone
import numpy as np
#import pandas as pd

import json
from django.http import JsonResponse




def index(request):
    #num = DataSolar.objects.last()
    today1 = datetime.date.today()
    num = DataSolar.objects.all().filter(days=today1).order_by('-id')[ :10]
    #print(num)
    context= { "num":num}
    return render(request, 'iotSolar/index.html', context)


def autohtml(request):
    todays = datetime.date.today()
    num = DataSolar.objects.last()
    context= { "num":num}
    return render(request, 'iotSolar/autoload.html', context)


def autoupload(request):
    num = DataSolar.objects.last()
    numSerial = serializers.serialize('json', [ num, ])
    return JsonResponse({'numSerial' : numSerial}, status=200)


'''
def index(request):
	dataSolars = dataSolar.objects.get(id=2)
	obj = DataSolar.objects.all()[-4:]
	now = datetime.datetime.now().strftime('%H:%M:%S')
	obj = DataSolar.objects.all().filter(hourly=now)
	obj = DataSolar.objects.order_by('id').last()
	obj = DataSolar.objects.last()

	context= {"data":obj}	
	return render(request, 'iotSolar/index.html', context)


def index(request):
    for d in  DataSolar.objects.all():
        v = d.voltage
        i = d.currents
        t = d.temp
        ins = d.intensity
        da = d.days
        h = d.hourly
        p = d.power
    
    context= {'da':da, 'h':h, 'p':p, 'ins':ins, 't':t, 'i':i, 'v':v}
    print(context)
    return render(request, 'iotSolar/index.html', context)

'''

def dataMaxMin(request):
    try:
        todays = datetime.date.today()
        volt = []
        amp = []
        temp = []
        intens = []
        times = []
        power = []
        objs = DataSolar.objects.all().values('voltage','hourly','currents','power','temp','intensity').filter(days=todays)
        for obj in objs:
            volt.append(obj['voltage'])
            amp.append(obj['currents'])
            temp.append(obj['temp'])
            intens.append(obj['intensity'])
            power.append(obj['power'])
            times.append(obj['hourly'])
        objsVolt = np.array(volt)
        objsAmp = np.array(amp)
        objstemp = np.array(temp)
        objsInten = np.array(intens)
        objsPower = np.array(power)
        max_volt = np.max(objsVolt)
        min_volt = np.min(objsVolt)
        max_amp = np.max(objsAmp)
        min_amp = np.min(objsAmp)
        max_temp = np.max(objstemp)
        min_temp = np.min(objstemp)
        max_ints = np.max(objsInten)
        min_ints = np.min(objsInten)
        max_power = np.max(objsPower)
        min_power = np.min(objsPower)
        return JsonResponse(data = {'max_volt' : max_volt,'min_volt': min_volt, 'max_amp' : max_amp,'min_amp': min_amp, 'max_temp' : max_temp, 'min_temp': min_temp,
                                'max_ints' : max_ints,'min_ints': min_ints, 'max_power' : max_power,'min_power': min_power,
                                'times': times,
                                }, status=200)
    except:
        return JsonResponse(data = {'max_volt' : 0,'min_volt': 0, 'max_amp' : 0,'min_amp': 0, 'max_temp' : 0, 'min_temp': 0,
                                'max_ints' : 0,'min_ints': 0, 'max_power' : 0,'min_power': 0,
                                'times': datetime.date.today(),
                                }, status=200)      
    

def voltageChart(request):
	today1 = datetime.date.today()
	obj = DataSolar.objects.all().filter(days=today1)
	context= {
		"data":obj
	}	
	return render(request, 'iotSolar/chart/voltChart.html', context)


def voltageChartt(request):
	today1 = datetime.date.today()
	labels = []
	data = []
	obj = DataSolar.objects.all().values('voltage','hourly').filter(days=today1)
	for entry in obj:
		labels.append(entry['hourly'])
		data.append(entry['voltage'])
	return JsonResponse(data={
		'labels': labels,
		'data' : data,
	})


def currentChartt(request):
	today1 = datetime.date.today()
	labels = []
	data = []
	objs = DataSolar.objects.all().values('currents','hourly').filter(days=today1)
	for entry in objs:
		labels.append(entry['hourly'])
		data.append(entry['currents'])
	return JsonResponse(data={
		'labels': labels,
		'data' : data,
	})


def currentChart(request):
	today1 = datetime.date.today()
	obj = DataSolar.objects.all().filter(days=today1)
	context= {
		"data":obj
	}	
	return render(request, 'iotSolar/chart/currentChart.html', context)	


def faultChart(request):
	obj = DataSolar.objects.all()
	context= {
		"data":obj
	}	
	return render(request, 'faultChart.html', context)


def powerChartt(request):
	today1 = datetime.date.today()
	labels = []
	data = []
	obj = DataSolar.objects.all().values('power','hourly').filter(days=today1)
	for entry in obj:
		labels.append(entry['hourly'])
		data.append(entry['power'])
	return JsonResponse(data={
		'labels': labels,
		'data' : data,
	})


def powerChart(request):
    today1 = datetime.date.today()
    obj = DataSolar.objects.all().filter(days=today1)
    context= {
		"data":obj
	}	
    return render(request, 'iotSolar/chart/powerChart.html', context)	


def intenChartt(request):
	today1 = datetime.date.today()
	labels = []
	data = []
	obj = DataSolar.objects.all().values('intensity','hourly').filter(days=today1)
	for entry in obj:
		labels.append(entry['hourly'])
		data.append(entry['intensity'])
	return JsonResponse(data={
		'labels': labels,
		'data' : data,
	})
 

def intenChart(request):
    today1 = datetime.date.today()
    obj = DataSolar.objects.all().filter(days=today1)
    context= {
		"data":obj
	}	
    return render(request, 'iotSolar/chart/intenChart.html', context)


def tempChartt(request):
	today1 = datetime.date.today()
	labels = []
	data = []
	obj = DataSolar.objects.all().values('temp','hourly').filter(days=today1)
	for entry in obj:
		labels.append(entry['hourly'])
		data.append(entry['temp'])
	return JsonResponse(data={
		'labels': labels,
		'data' : data,
	})	


def tempChart(request):
    today1 = datetime.date.today()
    obj = DataSolar.objects.all().filter(days=today1)
    context= {
		"data":obj
	}	
    return render(request, 'iotSolar/chart/tempChart.html', context)


class ServiceGenericAPIView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = SolarDataSerializer
    queryset = DataSolar.objects.all()
    lookup_field = 'hourly'

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id =None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

