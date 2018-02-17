import requests

proxies = {
         'http' : 'http://35.231.108.164:8888',
         'https' : 'https://35.231.108.164:8888',
        }  


source = requests.get('http://chicago.craigslist.org/search/cto?query=ford+mustang&sort=rel&max_price=5000&min_auto_year=2001', proxies=proxies)
print(source.history)

ime = source.history[0].headers['x-cache-proxyname']
print(ime)