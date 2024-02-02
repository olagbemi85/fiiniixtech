"""fiiniixtech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls',namespace='home')),
    path('shop/', include('shop.urls',namespace='shop')),
    #path('solarproject/', include('myproject1.urls',namespace='solarproject')),
    path('basket/', include('basket.urls',namespace='basket')),
    path('authentication/', include('authentication.urls',namespace='authentication')),
    path('solarIot/', include('iotSolar_proj.urls',namespace='iotSolar')),
    path('smart-power-network/', include('iotPowerSystem.urls',namespace='smartpower')),
    path('chat/', include('chat.urls',namespace='chat')),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)



admin.site.index_title=" fiiniix tech. site "
admin.site.site_header="fiiniixtech"
admin.site.site_title= "fiiniixtech"                         