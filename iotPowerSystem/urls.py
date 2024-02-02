from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'iotPowerSystem'


urlpatterns = [
    path('sps/', index, name='home'),
    #path('sps/', Dashboard.as_view(), name='home'),
    path('spsd/', StationDetails.as_view(), name='spsdata'),
    path('sps/register/', profileRegister, name='register'),
    path('sps/station-register/', stationRegister, name='sta_register'),
    path('spower/', smartpower, name='spower'),
    path('auto/<slug:slug>', autoupload, name='auto'),
    path('currentChart', currentChart, name='currentChart'),
    path('voltageChart', voltageChart, name='voltageChart'),
    path('powerChart', powerChart, name='powerChart'),
    path('tempChart', tempChart, name='tempChart'),
    path('detail/<slug:slug>/', station_detail, name='station_detail'),
    path('spspage/<slug:slug>/', station_data_detail, name='sps_page'),
    path('spsdetail/<slug:slug>/', get_spsdata, name='sps_data'),
    path('power/<slug:slug>/', xter_power, name='xterpower'),
]
