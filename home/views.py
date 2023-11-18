from django.shortcuts import render
from channels.layers import get_channel_layer
from time import sleep

# Create your views here.

async def home(request):
    chnanel_layer = get_channel_layer()
    for i in range(1,10):
       await chnanel_layer.group_send(
            'new_consumer_group',{
                'type':'send_notification',
                'value': i
            }
        )
       sleep(.1)
    return render(request, 'home.html')