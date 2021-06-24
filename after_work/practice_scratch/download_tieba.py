'''import urllib.request
import re


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html


def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'

    imglist = re.findall(p,html)
    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve((each,filename,None))
        print(each)

if __name__ == '__maain__':
    url = 'https://tieba.baidu.com/p/6603249549'
    get_img(open_url(url))'''




import urllib.request
import re


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html


def get_img(html):
    p = r'(([0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}([0,1]?\d?\d|2[0-4]\d|25[0-5])'

    iplist = re.findall(p,html)
    for each in iplist:
        print(each)

if __name__ == '__maain__':
    url = 'http://cn-proxy.com'
    get_img(open_url(url))




























































