import urllib.request
import random

iplist = ['117.88.176.110:3000','221.206.100.133:34073','119.41.236.180:8010']
url = 'http://45.32.164.128/ip.php'
#url = 'https://www.whatismyip.com.tw/ '
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')]
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)










































