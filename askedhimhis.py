import requests



proxies = {
    'http' : 'http://73.111.144.9:8888',
    'https' : 'https://73.111.144.9:8888',
}


r = requests.get('http://73.111.144.9:8889/', proxies=proxies )


ime = r.headers['x-cache-proxyname']
print(ime)

payld = {
    'name' : ime,
}
headers={'Authorization' : 'c2FtZXJ6'}

stop = requests.post('http://73.111.144.9:8889/api/instances/stop', json=payld,headers=headers)

print(stop.text)