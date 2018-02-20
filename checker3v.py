import threading,random
import requests
import logging
import bs4 as bs
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
global nisam
global prox
global kekec
global url
global serchurl
global mek
global cities
global numic
global Bool
#Bzeaiter@gmail.com
def send_simple_message(text):
    return requests.post(
        "https://api.mailgun.net/v3/clcrawler.com/messages",
        auth=("api", "key-c81f33bf13419f1536ffbf09ae3054f0"),
        data={"from": "Python CL<mailgun@clcrawler.com>",
              "to": ["Bzeaiter@gmail.com"],
              "subject": "New car",
              "text": text})
def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login('zeaitirsamer5@gmail.com', 'Samerz2010')
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        try:
            print("failed to send mail, sending through another account")
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print('successfully sent the mail')
        except:
            send_simple_message(message)
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
        if(prox[0]!="'"):
            poxy = "'" + prox + "'"
            proxylist = '[' + poxy + ']' 
        else:
            proxylist = '[' + prox + ']'
        #print(proxylist)
        proxylist = ast.literal_eval(proxylist)
        #print(proxylist)
        proxy = random.choice(proxylist)
        #print(proxy)
        #pd = 
        proxies = {
         'http' : 'http://' + proxy + ':8888',
         'https' : 'https://' + proxy + ':8888',
        }  
        #print(ip)
        return proxies
#http://user:pass@10.10.1.10:3128/
dicti = {}
#python allthreads.py Texas,Alabama 1 'https://chicago.craigslist.org/search/cto?query=ford+mustang'
#proxies = getproxy()


def carscrap(link):
                
            #print(kekec)
            #threadLock.acquire()
            #threadLock.acquire()
                the_link = 'http://' + link + serchurl
                print(the_link)
            #href = link.get('href') #state searcher
            #mehurl = href + serchurl
            #print(mehurl)
                #proxies=getproxy()
                try:
                    proxies=getproxy()
                    headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)'}    
                    source = requests.get(the_link,timeout=6.5,proxies=proxies,headers = headers)
                    content = (source.content.decode("utf-8"))
                    #print("Scraping " + the_link + " with IP: " + proxies['http'] + "\n")
                #    print(content)

                    if (content.find('This IP has been') == 0):
                         print ("BLOCKED")
                         logging.warning("IP Blocked")
                    #print(content)
                         print(source.history)
                         ime = source.history[0].headers['x-cache-proxyname']
                         payld = {
                            'name' : ime,
                         }
                         headers={'Authorization' : 'c2FtZXJ6'}
                         ipic = proxies.get('http')
                         ipic = ipic[0:-1] + '9'
                         print(ipic)
                         stop = requests.post(ipic + '/instances/stop', json=payld,headers=headers)
                         raise EnvironmentError
                except EnvironmentError:
                    print("PROXY ERROR AT:" + link)
                    nisam.remove(link)
                    sys.exit()
                    logging.warning("PROXY ERROR")
                    
                else:
                #the_link = 'https://' + link + serchurl
            #threadLock.release()
                    soup = bs.BeautifulSoup(source.text, 'lxml')
            #print(mehurl)
                    #print(link + ":")
                    idlist = []
                    for id in soup.find_all('p', class_='result-info'):
                        dat = id.find('a')
                        urlic = (dat.get('href'))
                        #print(dat.get('data-id'))
                        idlist.append(int(dat.get('data-id')))
                    dicti[link] = idlist
                    #print("nisam)
                    nisam.remove(link)
                    #print(dicti[link])
                    #print("\n\n CITIES:", cities[link])
                    #print(type(cities[link]))
                    if(dicti[link] != cities[link]):
                        for ded in dicti[link]:
                            if ((cities[link]==[] and dicti[link]!=[]) or not(ded in cities[link])):
                                #slen = urlic.find('cto')
                                bab = soup.find(attrs={"data-pid" : ded})
                                price = bab.find('span', class_='result-price')
                                if (price is None):
                                    price = 'no price'
                                else:
                                    price = price.text
                                babic = soup.find('a',attrs={"data-id" : ded} )
                                title = babic.text
                                href = babic['href']
                                carurl = href
                                print("Sending an email, URL: ", carurl)
                                logging.info("Sent an email, STATE: %s, ID: %s", link, babic)
                               # carurl = 'https://' + link + '.craigslist.org/' + 'cto/d' + '/randomname/' + ded + '.html'
                                #carweb = requests.get(carurl)
                                #soup = bs.BeautifulSoup(carweb.text, 'lxml')
                                #print(soup)
                                carinf = title + " - " + price
                                #carsinfo = carsinfo + "Price: " + price + "\nTitle: " + title + "\nCity: " + link + "\nLink: " + carurl + "\n"
                                message = "Price: " + price + "\nTitle: " + title + "\nCity: " + link + "\nLink: " + carurl
                                send_email('zeaitirsamer5@gmail.com','Samerz2010','Bzeaiter@gmail.com',carinf,message)
                                print("\n\nEmail SENT\n\n", carurl)
                                cities[link].append(ded)
                                
                                
                                
                            elif ded in cities[link]:
                                print("nuffin")
                                pass
                    #print('vozi')
                    #print("dd;", nisam)
                        if(nisam==[]):
                            print(car.link)
                            print("WTF?")
                            #print("b4" + str(car.cities))
                            car.cities = (cities)
                            #print("after" + str(car.cities))
                            logging.info("Saved %s", car.name)
                            car.save()
                            
                            mek = True
                        #carsinfo = ''
                   # print("\n\nstates left to scrap:", nisam)
class MyThread (threading.Thread):
   def __init__(self, statelist):
      threading.Thread.__init__(self)
      self.statelist = statelist
   def run(self):
      # Get lock to synchronize threads
      #threadLock.acquire()
      carscrap(self.statelist)

      if self in threads:
            print("stopping: ", self.statelist)
            #rint('kekec')
            threads.remove(self)

            #print('kekec')
           
            self.stopped = True
      # Free lock to release next thread
      #threadLock = threading.Lock()
      #threadLock.release()
threads = []
threadLock = threading.Lock()
#nisam = get_state('Texas')
#mek = get_state('Massachusetts')
#nisam = nisam + mek
#length = len(nisam)
#nisam = get_state(states)
#lengthd = len(nisam)
def check(length):
    for i in nisam:
        thread1=MyThread(i)
        thread1.start()
        threads.append(thread1)


def main(states,url):
    #citylist=[]
    #global idk
    
    

   
    global serchurl
    global nisam
    global kekec
    global bool
    global prox 
    pd = Podesavanja.objects.get(id=1)
    prox = pd.proxylist
    bool = False
    kekec=url
    #idk=int(idk)
    #print(idk)
    nisam = []
    #accept id as well
#   print(url)
    url = url + '&postedToday=1&searchNearby=1'
    serch = (url.find('craig'))
    lengthurl = len(url)
    serchurl = '.' + (url[serch:lengthurl])
    strlength = len(states)
    states = states[1:strlength-1]
    states = states.replace("'", "")
    states = states.replace(", ", ",")
    #print(states)
    states = states.split(',')
    #print(states)
    print("main")
    for state in states:
        nisam = nisam + (get_state(state))
    length = len(nisam)
    print("states are" + str(nisam))
    check(length)
while(1):
    logging.basicConfig(filename='crawler.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    Cars = CarModel.objects.all()
    while(1):
        pd = Podesavanja.objects.get(id=1)
        if(pd.status=='Stop'):
            print("\nStopping the crawlers per order, checking every minute\n")
            time.sleep(60)
        else:
            break 

    if(Cars==None):
        print("Waiting for cars")
        time.sleep(8)
        Cars = CarModel.objects.all()
    for car in Cars:
        print("\n\n Scraping again \n\n")
        mek = False
        readable = time.ctime()
        logging.info("Scraping again MODEl:  %s", car.name)

        print("Waiting for 3 seconds, ", readable)
        time.sleep(3)
        link = car.link
        states = car.states
        print("STATES: " + states)
        cities = car.cities
        try:
            cities = ast.literal_eval(cities)
        except:
            print("waiting on the website")
            time.sleep(9)
            car = CarModel.objects.get(link=link)
            cities = car.cities
            cities = ast.literal_eval(cities)
        print("CITIES   : " + str(cities) + "  type:  " + str(type(cities)))
        main(states,link)
        while(1):
          try:
            if(mek):
                print("Saving")
                
                break
            if(threads==[]):
                print("No more threads")
                print("database:", str(cities))
                #car.cities = (cities)
               # car.save()
                break
            else:
                #a = a+1
                #print("Continuing", a)
                logging.info("Else, 330")
                continue
          except:
              print("Module error [0]")