from django.db import models
import json
from datetime import datetime
# Create your models here.
class CarModel(models.Model):
    link = models.URLField(unique=False, max_length=2000)
    #email = models.EmailField(unique=False) #Set to False so Bot can use same email adress all over again, contact me if you want it to be set to True.
    #is_active = models.BooleanField(default=True)
    states = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=datetime.now())
    cities = models.CharField(max_length=100000)
    def setstates(self, x):
        self.states = json.dumps(x)
    def getstates(self):
        return json.loads(self.states)
