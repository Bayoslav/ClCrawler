proxy = '104.199.117.46'
import requests
proxies = {
         'http' : 'http://' + proxy + ':8888',
         'https' : 'https://' + proxy + ':8888',
        }  

source = requests.get('http://chicago.craigslist.org/search/cto?query="highlander"+%7C+"high+lander"+%7C+"rx300"+%7C+"rx+300"+%7C+"rx330"+%7C+"rx+330"+%7C+ls430+%7C+"ls+430"+%7C+"rav4"+%7C+"rav-4"+%7C+"rav+4"+%7C+"gx470"+%7C+"lx470"+%7C+"2009+corolla"+%7C+"2010+corolla"&sort=rel&max_price=5500&min_auto_year=2001',proxies=proxies)
print(source.history)
ime = source.history[0].headers['x-cache-proxyname']
print(ime)
headers={'Authorization' : 'c2FtZXJ6'}
ipic = proxies.get('http')
ipic = ipic[0:-1] + '9'
print(ipic)