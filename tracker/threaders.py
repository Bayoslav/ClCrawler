import threading
from allthreads import check
import requests
import bs4 as bs
import json
import threading
from stateslist import get_state
import time

url = 'https://chicago.craigslist.org/search/cto?query=ford+mustang&postedToday=1&searchNearby=1' #&postedToday=1
serch = (url.find('craig'))
length = len(url)
serchurl = '.' + (url[serch:length])
#classheight3 geo-site-list
#states = ['AL']
def getproxy():
    r = requests.get('http://api.proxyrotator.com/?apiKey=xPEjwuFkAhRrX2v43ZgVzcMWpQ9Gfs8H&speed=10')
    dt = r.json()
    kip = dt.get('proxy')
    #kip = '85.26.146.169:80'
    ip = 'http://' + kip
    httpsprox = 'https://' + kip
    proxies = {
        "http" : ip,
        "https" : httpsprox,
        #"https" : httpsprox,
        #'https' : httpsprox,
    }
    #print(ip)
    return proxies
'''def statescrap(states):
    start_time = time.time()
    urllist =  {}
    for state in states:
        stateurl = 'http://geo.craigslist.org/iso/us/' + state + serchurl
        proxies = getproxy()
        statesauce = requests.get(stateurl, proxies=proxies).text
        supa = bs.BeautifulSoup(statesauce, 'lxml')
        statelist = supa.find('div',class_='geo-site-list-container')
        #print("kek")
        #print(statelist)
        bb = statelist.find_all('a')
        return bb'''
def carscrap(bb):
        for link in bb:
            threadLock.acquire()
            proxies = getproxy()
            threadLock.release()
            the_link = 'https://' + link + serchurl
            #href = link.get('href') #state searcher
            #mehurl = href + serchurl
            #print(mehurl)
            print(the_link)
            try:
                source = requests.get(the_link, proxies=proxies)
            except:
                print("PROXY ERROR AT:" + link)
                proxies = getproxy()
                #the_link = 'https://' + link + serchurl
                try:
                    source = requests.get(the_link, proxies=proxies)
                except:
                    print("PROXY ERROR AT:" + link)
                    proxies = getproxy()
                    #the_link = 'https://' + link + serchurl
                    try:
                        source = requests.get(the_link, proxies=proxies)
                    except:
                        print("CANT SCRAP" + link + "AFTER 3 TRIES")

            soup = bs.BeautifulSoup(source.text, 'lxml')
            #print(mehurl)
            print(link + ":")
            for id in soup.find_all('p', class_='result-info'):
                dat = id.find('a')
                print(dat.get('data-id'))
nisam = get_state('Texas')
kek = get_state('Alabama')
mek = get_state('California')
nisam = nisam
#carscrap(nisam)
k=0
#tuple(nisam)
#_thread.start_new_thread( carscrap, (nisam ))
threadLock = threading.Lock()
threads = []
length = len(nisam)
#threadLock = threading.Lock()
#length = len(nisam)
check(length)
# Wait for all threads to complete

for t in threads:
    t.join()
print ("Exiting Main Thread")
