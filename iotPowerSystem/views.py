from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework import mixins
from .models import *
from .forms import *
from django.http import JsonResponse
import datetime
from authentication.models import Notification

from django.core import serializers
import numpy as np
from django.views.generic.list import ListView
from django.views import View
from django.utils import timezone
from authentication.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

import json
from django.http import JsonResponse
from django.contrib import messages

'''
class Dashboard(View, LoginRequiredMixin):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            f_requests = UserProfile.objects.filter(user = user)
            #print(user)
            
            try:
                r_company = Company.objects.filter(name = f_requests.company)
                if request.user.is_superuser:
                    station = Station.objects.all()
                    return render(request, 'iotPowerSystem/frontpage.html',{'station':station})
                
                #f_requests = UserProfile.objects.filter( company=r_company.name)
                #st = Station.objects.all()

                elif r_company or f_requests.staff_level == 'CCO':
                    station = Station.objects.filter(company=f_requests.company)
                    return render(request, 'iotPowerSystem/frontpage.html',{'station':station})

                        elif f_requests.company == s.company and f_requests.regional_office == s.regional_office:
                            station = Station.objects.filter(regional_office = f_requests.regional_office)
                            return render(request, 'iotPowerSystem/frontpage.html',{'station':station})
                        elif f_requests.company == s.company and f_requests.regional_office==st.regional_office and f_requests.area_office == s.area_office:
                            station = Station.objects.filter(regional_office = f_requests.area_office)
                            return render(request, 'iotPowerSystem/frontpage.html',{'station':station})
                        elif f_requests.company == s.company and f_requests.regional_office==st.regional_office and f_requests.staff_position == 'Service Engineer':
                            station = Station.objects.filter(regional_office = f_requests.area_office)
                            return render(request, 'iotPowerSystem/frontpage.html',{'station':station})

            except:
                profile_form = UserSPSForm(request.POST, instance=request.user.userprofile)
                context = {'profile_form':profile_form}
                return render(request, 'iotPowerSystem/pages/profileRegister.html', context) 
        else:
            return redirect('authentication:userlogin')
        
        
    def post(self, request):
        if request.method == 'POST':
            profile_form = UserSPSForm(request.POST, instance=request.user.userprofile)

            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect('smartpower:home')    
'''


@login_required
def index(request):
    if request.user.is_authenticated:
        user = request.user
        profile = UserProfile.objects.get(user=user)
        #print(profile.company)
        pp= get_object_or_404(UserProfile, user=user)
        #try: 
        
        if request.user.is_superuser:
            station = Station.objects.all()
            context={'station':station}
            return render(request, 'iotPowerSystem/frontpage.html',context)
        elif pp.staff_position=="DISPATCH" or pp.staff_position=="MTECH":
            station = Station.objects.filter(regional_office = profile.regional_office)
            #st1 = Station.objects.get(regional_office = profile.regional_office)
            #data = Data.objects.filter(station_code = st1.code)
            return render(request, 'iotPowerSystem/frontpage.html',{'station':station})
        elif pp.staff_position=="SMD":
            station = Station.objects.filter(area_office = profile.area_office)
            #st2 = Station.objects.get(area_office = profile.area_office)
            #data = Data.objects.filter(station_code = st2.code)
            return render(request, 'iotPowerSystem/frontpage.html',{'station':station})
        elif pp.staff_position=="SERVICE ENGINEER":
            station = Station.objects.filter(profile = profile)
            #st3 = Station.objects.get(profile = profile)
            #data = Data.objects.filter(station_code = st3.code)
            return render(request, 'iotPowerSystem/frontpage.html',{'station':station})
        elif pp.staff_position=="HQ":
            station = Station.objects.filter(copmany = profile.company)
            #st4 = Station.objects.get(copmany = profile.company)
            #data = Data.objects.filter(station_code = st4.code)
            return render(request, 'iotPowerSystem/frontpage.html',{'station':station})
        else:
            messages.warning(request, 'User not registar')  
            return redirect('smartpower:register')
            
        #finally:
        #    messages.warning(request, 'User not registar')  
            #return redirect('smartpower:sta_register')
        #    return redirect('smartpower:register')

    else:
        return redirect('authentication:userlogin')                          


@login_required
def profileRegister(request):
    profile_form = UserSPSForm(request.POST, instance=request.user.userprofile)
    context = {'profile_form':profile_form}
    if profile_form.is_valid():
        profile_form.save()
        messages.success(request, 'Your profile is updated successfully')
        return redirect('smartpower:home')
    return render(request, 'iotPowerSystem/pages/profileRegister.html', context)


@login_required
def stationRegister(request):
    station_form = StationForm(request.POST)
    context = {'station_form':station_form}
    if station_form.is_valid():
        station_form.save()
        messages.success(request, 'Your profile is updated successfully')
        return redirect('smartpower:home')
    return render(request, 'iotPowerSystem/pages/stationRegister.html', context)


def station_detail(request, slug):
    station = get_object_or_404(Station, code=slug)
    #return render(request, 'iotPowerSystem/pages/station_details.html', {'station': station})
    return render(request, 'iotPowerSystem/pages/stationDetail.html', {'station': station})


def station_data_detail(request, slug):
    #data = get_object_or_404(Data, station_code=slug)
    data = Data.objects.filter(station_code = slug)
    station = slug
    return render(request, 'iotPowerSystem/pages/station_data.html', {'data': data, 'st':station})


@login_required	
def smartpower(request):
    try:
        todays = datetime.date.today()
        power_r = []
        power_y = []
        power_b = []
        temp = []
        station_code = []
        times = []
        days = []
       
        objs = Data.objects.all().values('power_r','power_y','power_b','temp','station_code','hourly').filter(hourly=+todays)
        for obj in objs:
            power_r.append(obj['power_r'])
            power_y.append(obj['power_y'])
            power_b.append(obj['power_b'])            
            temp.append(obj['temp'])
            station_code.append(obj['station_code'])
            times.append(obj['hourly'])
        return JsonResponse(data = {'power_r' : power_r,'power_y': power_y, 'power_b' : power_b,'temp': temp, 'station_code' : station_code, 'times': times, 
                                
                                }, status=200)
    except:
        return JsonResponse(data = {'power_r' : 0,'power_y': 0, 'power_b' : 0,'temp': 0, 'station_code' : 0, 'times': todays, 
                                
                                }, status=200)


@login_required
def autoupload(request, slug):
    try:
        num = Data.objects.filter(station_code = slug).last()
        numSerial = serializers.serialize('json', [ num ])
        return JsonResponse({'numSerial' : numSerial}, status=200)
    except:
        messages.warning(request, 'no data recieve from the station')
        return redirect('smartpower:home')

@login_required
def xter_power(request, slug):
    st = Station.objects.get(code = slug)
    num = Data.objects.filter(station_code = slug).last()
    s_cod = num.station_code
    sum_power = num.power_b+num.power_r+num.power_y
    max_power = (sum_power*1.732*0.8)/3
    power_percent = (max_power/st.max_power)*100
    power_percent = str(power_percent)
    max_p = power_percent + "%"
    numSerial = json.dumps(max_p)   #json.dumps() function will convert a subset of Python objects into a json string. Not all objects are convertible and you may need to create a dictionary of data you wish to expose before serializing to JSON.
    #data = json.loads(request.body) #from fastAPI body: JSON.stringify(data) #json.load() : it accepts a file object. To read JSON data from a file and convert it into a dictionary
    #numSerial = serializers.serialize('json', max_power)
    s_code = json.dumps(s_cod)
    return JsonResponse({'numSerial' : numSerial, 's_code':s_code}, status=200)



@login_required
def currentChart(request):
	today1 = datetime.date.today()
	labels = []
	data_r = []
	data_y = []
	data_b = []
	objs = Data.objects.all().values('currents_r', 'currents_y', 'currents_b', 'hourly').filter(days=today1).order_by('-id','station_code')[:10]
	for entry in objs:
		labels.append(entry['hourly'])
		data_r.append(entry['currents_r'])
		data_y.append(entry['currents_y'])
		data_b.append(entry['currents_b'])
	return JsonResponse(data={
		'labels': labels,
		'data_r' : data_r, 'data_y' : data_y, 'data_b' : data_b,
	})

@login_required
def voltageChart(request):
	today1 = datetime.date.today()
	labels = []
	data_r = []
	data_y = []
	data_b = []
	objs = Data.objects.all().values('voltage_r', 'voltage_y', 'voltage_b', 'hourly').filter(days=today1).order_by('-id','station_code')[:10]
	for entry in objs:
		labels.append(entry['hourly'])
		data_r.append(entry['voltage_r'])
		data_y.append(entry['voltage_y'])
		data_b.append(entry['voltage_b'])
	return JsonResponse(data={
		'labels': labels,
		'data_r' : data_r, 'data_y' : data_y, 'data_b' : data_b,
	})

@login_required
def powerChart(request):
	today1 = datetime.date.today()
	labels = []
	data_r = []
	data_y = []
	data_b = []
	objs = Data.objects.all().values('power_r', 'power_y', 'power_b', 'hourly').filter(days=today1).order_by('-id','station_code')[:10]
	for entry in objs:
		labels.append(entry['hourly'])
		data_r.append(entry['power_r'])
		data_y.append(entry['power_y'])
		data_b.append(entry['power_b'])
	return JsonResponse(data={
		'labels': labels,
		'data_r' : data_r, 'data_y' : data_y, 'data_b' : data_b,
	})
 
@login_required
def tempChart(request):
	today1 = datetime.date.today()
	labels = []
	data = []
	
	objs = Data.objects.all().values('temp' 'hourly').filter(days=today1).order_by('-id','station_code')[:10]
	for entry in objs:
		labels.append(entry['hourly'])
		data.append(entry['temp'])
	return JsonResponse(data={
		'labels': labels,
		'data' : data,
	})


class StationDetails(View):
    def get_model(self):
        models = get_object_or_404(Station, code=self.slug)
        try:
            today1 = datetime.date.today()
            labels = []
            volt_r = []
            volt_y = []
            volt_b = []
            amp_r = []
            amp_y = []
            amp_b = []
            av_r = []
            av_y = []
            av_b = []
            temp = []
            time = []
            objs = Data.objects.all().values('voltage_r', 'voltage_y', 'voltage_b','currents_r', 'currents_y', 'currents_b','power_r', 'power_y', 'power_b', 'temp', 'hourly').filter(days=today1, station_code=models.code).order_by('-id','station_code')[:10]
            for entry in objs:
                labels.append(entry['hourly'])
                volt_r.append(entry['voltage_r'])
                volt_y.append(entry['voltage_y'])
                volt_b.append(entry['voltage_b'])
                amp_r.append(entry['currents_r'])
                amp_y.append(entry['currents_y'])
                amp_b.append(entry['currents_b'])
                av_r.append(entry['power_r'])
                av_y.append(entry['power_y'])
                av_b.append(entry['power_b'])
                temp.append(entry['temp'])
                time.append(entry['hourly'])
            return JsonResponse(data={
                'labels': labels,
                'volt_r' : volt_r, 'volt_y' : volt_y, 'volt_b' : volt_b,
                'amp_r' : amp_r, 'amp_y' : amp_y, 'amp_b' : amp_b,
                'av_r' : av_r, 'av_y' : av_y, 'av_b' : av_b,'temp':temp, 'time':time,
            })
        except:
            return JsonResponse(data = {'labels': labels,
                'volt_r':0, 'volt_y':0, 'volt_b':0,
                'amp_r':0, 'amp_y':0, 'amp_b':0,
                'av_r':0, 'av_y':0, 'av_b':0 ,'temp':0, 'time':today1,
                                    
                                    }, status=200)


@login_required
def get_spsdata(request, slug):
    
        #data = get_object_or_404(Data, code=slug)
        #models = get_object_or_404(Station, code=slug)
        try:
            today1 = datetime.date.today()
            labels = []
            volt_r = []
            volt_y = []
            volt_b = []
            amp_r = []
            amp_y = []
            amp_b = []
            av_r = []
            av_y = []
            av_b = []
            temp = []
            time = []
            objs = Data.objects.all().values('voltage_r', 'voltage_y', 'voltage_b','currents_r', 'currents_y', 'currents_b','power_r', 'power_y', 'power_b', 'temp', 'hourly').filter(days=today1, station_code=slug).order_by('-id','station_code')[:10]
            for entry in objs:
                labels.append(entry['hourly'])
                volt_r.append(entry['voltage_r'])
                volt_y.append(entry['voltage_y'])
                volt_b.append(entry['voltage_b'])
                amp_r.append(entry['currents_r'])
                amp_y.append(entry['currents_y'])
                amp_b.append(entry['currents_b'])
                av_r.append(entry['power_r'])
                av_y.append(entry['power_y'])
                av_b.append(entry['power_b'])
                temp.append(entry['temp'])
                time.append(entry['hourly'])
            return JsonResponse(data={
                'labels': labels,
                'volt_r' : volt_r, 'volt_y' : volt_y, 'volt_b' : volt_b,
                'amp_r' : amp_r, 'amp_y' : amp_y, 'amp_b' : amp_b,
                'av_r' : av_r, 'av_y' : av_y, 'av_b' : av_b,'temp':temp, 'time':time,
            })
        except:
            return JsonResponse(data = {'labels': labels,
                'volt_r':0, 'volt_y':0, 'volt_b':0,
                'amp_r':0, 'amp_y':0, 'amp_b':0,
                'av_r':0, 'av_y':0, 'av_b':0 ,'temp':0, 'time':today1,
                                    
                                    }, status=200)

'''
@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UserSPSForm(request.POST, request.FILES, instance=request.user.userprofile)

        if profile_form.is_valid():
        #if user_form.is_valid() :
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('smartpower:home')
    else:
       	try:
            user_form = UserFormUpdate(instance=request.user)
            profile_form = UserProfileInfoForm(instance=request.user.userprofile)
        except:
            profile = UserProfileInfo.objects.create(user=request.user)
            user_form = UserFormUpdate(instance=request.user)
            profile_form = UserProfileInfoForm(instance=profile)
        

    return render(request, 'apps/authentication/forms/update_profile.html', {'user_form': user_form, 'profile_form':profile_form })
'''
#https://stackoverflow.com/questions/70421105/cannot-resolve-keyword-user-into-field-choices-are-create-account-email-fu
#https://www.google.com/search?client=firefox-b-d&q=%27Cannot+resolve+keyword+%27user%27+into+field.%27+error+after+creating+custom+User+model+class++and+call+%27+request.user+in+views.py+in+django+project
#f_requests = UserProfile.objects.filter(id=user.id)
#profile = UserProfile.objects.get(user=user)
#profile = UserProfile.objects.all().values('company','regional_office','area_office','staff_level','staff_position').filter(user=user)        
