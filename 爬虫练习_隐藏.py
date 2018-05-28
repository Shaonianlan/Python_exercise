import urllib.request
import random

url='http://www.whatismyip.com.tw'

iplist=['122.72.32.73:80','122.72.32.74:80','118.178.124.33:3128']

proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]

urllib.request.install_opener(opener)
response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)
