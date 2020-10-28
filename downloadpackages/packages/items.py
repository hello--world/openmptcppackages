# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DownloadItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field

class PackagesItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    is_dir = scrapy.Field()

