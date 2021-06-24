import urllib.request
import time


def open_url(url):
    # return htmlpage
    print(url)
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    response = urllib.request.urlopen(req)
    return response.read()


def getInitialpage():
    # return how many pages we have
    url = "http://jandan.net/ooxx"
    html = open_url(url)
    html = html.decode("utf-8")
    index = html.find("span class=\"current-comment-page\"")
    beginindex = html.find("[", index)
    endindex = html.find("]", index)
    initialpage = html[(beginindex + 1): endindex]
    return initialpage


def getpiclist(pageurl):
    html = open_url(pageurl)
    html = html.decode("utf-8")
    piclist = list()
    for i in range(html.count("[查看原图]</a><br /><img")):
        index = html.find("[查看原图]</a><br /><img")
        html = html[index:]
        beginindex = html.find("\"")
        endindex = html.find("\"", (beginindex + 1))
        picurl = html[beginindex + 1:endindex]
        html = html[endindex:]
        piclist.append(picurl)
    return piclist


def savepic(piclist):
    for picurl in piclist:
        html = open_url("http:{}".format(picurl))
        filename = picurl.split("/")[-1]
        print(filename)
        with open(filename, "wb") as f:
            f.write(html)
        time.sleep(1)


def test(page):
    initialpage = int(getInitialpage())
    for i in range((initialpage - page), (initialpage + 1)):
        pageurl = "http://jandan.net/ooxx/page-{}#comments".format(i)
        piclist = getpiclist(pageurl)
        savepic(piclist)


if __name__ == "__main__":
    test(1)
