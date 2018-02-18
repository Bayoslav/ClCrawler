import threading,random
import json,os,sys
import django
import ast
#ast.literal_eval https://chicago.craigslist.org/search/cto?query=yugo
import threading
from stateslist import get_state
from Scraptask import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Scraptask.settings")
django.setup()
from tracker.models import CarModel,Podesavanja
#global idk
import time
ipic = '344444:8888'
ipic = ipic[0:-1] + '9'
print(ipic)
try:
    pd = Podesavanja.objects.get(id=1)
except:
    lst = ['35.184']
    pd = Podesavanja.objects.create(proxylist='104.199.117.46',status='Start',id=1)
    pd.save()

