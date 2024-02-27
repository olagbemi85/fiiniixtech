'''
from channels.routing import ProtocolTypeRouter



application=ProtocolTypeRouter({
    
    
})
'''


from django.urls import path
from Authentication.consumers import *

websocket_urlpatterns = [
    #path('ws/notifications/', NotificationConsumer.as_asgi()),
]