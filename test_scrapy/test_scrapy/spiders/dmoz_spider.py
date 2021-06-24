import scrapy



class DmoztoolsSpider(scrapy.Spider):
    name = "dmoztools"
    allowed_domain = ['dmoztools.net']
    start_urls = [
        'http://dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://dmoztools.net/Computers/Programming/Languages/Python/Resources/'
    ]

    def parse(self,response):
        filename = response.url.split("/")[-2]

        with open(filename,'wb') as f:
            f.write(response.body)












