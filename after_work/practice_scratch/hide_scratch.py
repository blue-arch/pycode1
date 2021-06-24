import urllib.request
import urllib.parse
import json

content = input('请输入要翻译的内容')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

#第一种方法
'''head = {}
head['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
'''


data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15863531476562'
data['sign'] = 'f615e249e4b81ac5936ba621b54b3f12'
data['ts'] = '1586353147656'
data['bv'] = '901200199a98c590144a961dac532964'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'

data = urllib.parse.urlencode(data).encode('utf-8')

#第二种方法
'''req = urllib.request.Request(url,data)
req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
response = urllib.request.urlopen(req)'''

response = urllib.request.urlopen(url,data)

html = response.read().decode('utf-8')

print(html)

target = json.loads(html)
#print(type(target))

#print(target['translateResult'])

print("翻译结果为：%s" %(target['translateResult'][0][0]['tgt']))






