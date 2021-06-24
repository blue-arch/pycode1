import urllib.request

response = urllib.request.urlopen('http://placekitten.com/200/300')
#req = urllib.request.Request('http://placekitten.com/200/300') 实例化
#response = urllib.request.urlopen(req)
cat_img = response.read()

print(response.geturl())
print(response.info())
print(response.getcode())
with open('cat_200_300.jpg','wb') as f:
    f.write(cat_img)










