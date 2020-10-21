import scrapy


class DownloaSpider(scrapy.Spider):
    name = 'download'
    allowed_domains = ['openmptcprouter.com']
    start_urls = ['http://packages.openmptcprouter.com/', 'http://download.openmptcprouter.com/release']

    def parse(self, response):
        pass
