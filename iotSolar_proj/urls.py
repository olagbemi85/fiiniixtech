
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'iotSolar_proj'


urlpatterns = [
    path('solariot/', index, name='solariot'),
    path('auto', autoupload, name='auto'),
    path('autoll/', autohtml, name='autoll'),
    path('maxmin/', dataMaxMin, name='maxmin'),
    path('currentchart/', currentChart, name='currentchart'),
    path('voltchart/', voltageChart, name='voltchart'),
    path('powerchart/', powerChart, name='powerchart'),
    path('tempchart/', tempChart, name='tempchart'),
    path('intenchart/', intenChart, name='intenchart'),
    path('currentChartt', currentChartt, name='currentChartt'),
    path('voltageChartt', voltageChartt, name='voltageChartt'),
    path('powerChartt', powerChartt, name='powerChartt'),
    path('tempChartt', tempChartt, name='tempChartt'),
    path('inteneChartt', intenChartt, name='intenChartt'),
    path('data/', ServiceGenericAPIView.as_view(), name='data'),
    #path('solariot/', IndexView.as_view(), name='solariot'),
    
 
]
