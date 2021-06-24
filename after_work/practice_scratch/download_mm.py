import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request

def get_page(url):#得到当前页码
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')

    a = html.find("current-comment-page") + 23
    b = html.find(']',a)
    return (html[a:b])

def img_down(soup, n):# 解析soup并下载
    temp = 0
    text = soup.select('.view_img_link')
    imglist = []
    for i in text:
        imglist.append(i['href'])
        temp += 1
        if temp == n:
            break
    for i in imglist:
        tempurl = 'http:' + str(i)
        try:
            tempes = requests.get(tempurl, timeout=3)
        except requests.exceptions.ConnectionError:
            print('下载失败！')
            continue
        file_name = "picture" + '\\' + str(i)[23:] + ".jpg"  # 拼接图片名，picture为程序所在目录的文件夹
        print('正在下载：' + file_name)
        with open(file_name, 'wb') as f:
            f.write(tempes.content)
    print("此页下载完毕！")


url = 'http://jandan.net/ooxx' # 打开浏览器并登陆目标网址
browser = webdriver.Chrome()#浏览器的驱动需放在安装python的目录下
num = int(input('每页最大下载张数：'))
pages = int(input('下载几页：'))

page_num = int(get_page(url))+1#得到当前页码
for i in range(pages):
    page_num -= 1
    print(page_num)
    page_url = url + '/page-' + str(page_num) + '#comments'#拼出每页的网址
    browser.get(page_url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    print('正在下载第%d页'%page_num)
    img_down(soup,num)

browser.close()





















