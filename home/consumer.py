from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()
        self.send(text_data= json.dumps({'status':'connected from django channels'}))
        
    def receive(self, text_data):
        print(text_data)
        self.send(text_data= json.dumps({'status':'we got your data via django channels'}))
    
    def disconnect(self,*args, **kwargs):
        print('disconnect')

    def send_notification(self,event):
        print(event)
        notification = event.get('value')
        self.send(text_data= json.dumps(notification))
        
        
class Newconsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = "new_consumer"
        self.room_group_name = "new_consumer_group"
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({'status': 'connected new consumer'}))

    async def receive(self, data):
        
        await self.send(text_data= json.dumps({'status':data}))

        
    async def disconnect(self,*args, **kwargs):
        print('disconnected')
        
    async def send_notification(self,event):
        notification = event.get('value')
        await self.send(text_data= json.dumps(notification))