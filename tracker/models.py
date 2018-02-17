from django.db import models
import json
from datetime import datetime
# Create your models here.
class CarModel(models.Model):
    link = models.URLField(unique=False, max_length=2000)
    name = models.CharField(max_length=100,default='noname')
    lastscraped = models.DateTimeField(auto_now_add=True)
    #email = models.EmailField(unique=False) #Set to False so Bot can use same email adress all over again, contact me if you want it to be set to True.
    #is_active = models.BooleanField(default=True)
    states = models.CharField(max_length=5000)
    pause = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    cities = models.CharField(max_length=100000)
    def setstates(self, x):
        self.states = json.dumps(x)
    def getstates(self):
        return json.loads(self.states)

#class Settings(models.Model):
    
class Podesavanja(models.Model):
    proxylist = models.CharField(max_length=5000)
    STATUS_CHOICES = (('Start','Start'),
    ('Stop','Stop'),)
    status = models.CharField(choices = STATUS_CHOICES,max_length=40)
    