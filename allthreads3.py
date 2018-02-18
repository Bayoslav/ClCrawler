import threading
import requests
import bs4 as bs
import json,os,sys
import django
from stateslist import get_state
from Scraptask import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Scraptask.settings")
django.setup()
from tracker.models import CarModel
#global idk
import time
global nisam
global stejc
#global ime
global kekec
global url
global serchurl
global dicti
global imenche
#url = 'https://chicago.craigslist.org/search/cto?query=ford+mustang&postedToday=1&searchNearby=1' #&postedToday=1
#serch = (url.find('craig'))
#lengthurl = len(url)
#serchurl = '.' + (url[serch:lengthurl])
#python allthreads.py Texas,Alabama 1 'https://chicago.craigslist.org/search/cto?query=ford+mustang'
#classheight3 geo-site-list
#states = ['AL']
def getproxy():
        #23.254.75.31:21262,45.57.177.74:21318,45.57.181.244:21302,69.58.15.89:21240,23.254.75.203:21318
        #proxylist = ['23.254.75.31:21262','45.57.177.74:21318','45.57.181.244:21302','69.58.15.89:21240','23.254.75.203:21318']
        #proxy = random.choice(proxylist)
        proxies = {
        'http' : 'http://73.111.144.9:8888',
        'https' : 'https://73.111.144.9:8888',
        }
        #print(ip)
        return proxies
    #print(ip)
    #return proxies
dicti = {}
#python allthreads.py Texas,Alabama 1 'https://chicago.craigslist.org/search/cto?query=ford+mustang'
#proxies = getproxy()
nisam = []

def carscrap(link):
    while(1):
                  # print(kekec)
            #threadLock.acquire()
                 #threadLock.acquire()
                the_link = 'http://' + link + serchurl
                    #href = link.get('href') #state searche                    #mehurl = href + serchurl
            #print(mehurl)
                print(the_link)
              
              
                proxies = getproxy()
                headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)'}
                try:
                        source = requests.get(the_link,timeout=11.5,headers = headers)
                        #threadLock.release()
                        #print("Scraping " + the_link + " with IP: " + proxies['http'] + "\n")
                        
                except: 
                        print("ATTEMPTING", link)
                        
                else:
                    
                            
                #   print(content)
                    
                        #raise EnvironmentError
                #the_link = 'https://' + link + serchurl
            #threadLock.release()
                    soup = bs.BeautifulSoup(source.text, 'lxml')
            #print(mehurl)
                    print(link + ":")
                    idlist = []
                    for id in soup.find_all('p', class_='result-info'):
                        dat = id.find('a')
                        #print(dat.get('data-id'))
                        realid = (int(dat.get('data-id')))
                        idlist.append(realid)
                    dicti[link] = idlist
                    nisam.remove(link)
                    print(dicti[link])
                    print("\n\nstates left to scrap:" + str(nisam) + "kek")
                    
                    if(nisam!=[] and threads==[]):
                        lenig = len(nisam)
                        check(lenig)
                        break
                    if(nisam==[] and len(threads)<=1):
                        abk = dicti
                        print("ABK:      ", str(abk))
                        print("NISAM : ", str(nisam))
                        print(imenche)
                        Car = CarModel.objects.create(name=imenche,states=stejc,cities=abk,link=kekec)
                        #Car.cities = abk
                        Car.save()
                        break
                        print("Saving IDs\n")
                        sys.exit()
                        print("quit")
                    else: 
                        break
                    

class MyThread (threading.Thread):
   def __init__(self, statelist):
      threading.Thread.__init__(self)
      self.statelist = statelist
   def run(self):
      print ("Starting")
      # Get lock to synchronize threads
      #threadLock.acquire()
      carscrap(self.statelist)
      if self in threads:
            print("stopping: ", self.statelist)
            threads.remove(self)
            print("Length:", nisam)
            print(threads)
      #self.stopped = True
      # Free lock to release next thread
      #threadLock = threading.Lock()
      #threadLock.release()
threads = []
threadLock = threading.Lock() 
def check(length):
  for i in range(0,length,1):
    thread1=MyThread(nisam[i])
    thread1.start()
    threads.append(thread1)


def main(states,url,ime):
    #citylist=[]
    #global idk
    print("ALLTHREADS")
    global serchurl
    global nisam
    global kekec
    global stejc
    global dicti
    global imenche
    #global ime
    #global ime
    kekec=url
    dicti = {}
    print(nisam)
    print(ime)
    imenche = ime
    #idk=int(idk)
    #print(idk)
    nisam = []
    #accept id as well
    print(url)
    #ime=ime
    url = url + '&postedToday=1&searchNearby=1'
    serch = (url.find('craig'))
    lengthurl = len(url)
    serchurl = '.' + (url[serch:lengthurl])
    #states = states.split(',')
    #print(states)
    #states = states.split('')
    print(states)
    stejc = states
    for state in states:
        nisam = nisam + (get_state(state))
    length = len(nisam)
    print(nisam)
    check(length)
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SyntaxError("Insufficient arguments.")
    if len(sys.argv) != 4:
        # If there are keyword arguments
        main(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4])
        print("ker")
        print(sys.argv[4])
    else:
        # If there are no keyword arguments
        main(sys.argv[0], sys.argv[1])
