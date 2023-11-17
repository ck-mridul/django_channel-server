from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField()
    is_seen = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        chnanel_layer = get_channel_layer()
        notification_count = Notification.objects.filter(is_seen = False).count()
        data = {
            'count': notification_count, 
            'current_nottification' : self.notification
        }
        
        async_to_sync(chnanel_layer.group_send)(
            'test_consumer_group',{
                'type':'send_notification',
                'value': data
            }
        )
        super(Notification,self).save(*args, **kwargs)