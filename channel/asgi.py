
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from home.consumer import TestConsumer,Newconsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channel.settings')

# application = get_asgi_application()

ws_patterns = [
    path('ws/test/',TestConsumer.as_asgi()),
    path('ws/new/',Newconsumer.as_asgi())
    
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_patterns),
    "http": get_asgi_application(),
})