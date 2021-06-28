from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    
    # def __str__(self):
    #     return self.name

class Message(models.Model):
    msg = models.CharField(max_length=300)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)