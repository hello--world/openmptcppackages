import scrapy
from scrapy.http import Response
from downloadpackages.packages.items import PackagesItem
from downloadpackages.log import log
# from scrapy_redis.spiders import RedisSpider

Version = 'v0.58.4'

class PackageSpider(scrapy.Spider):
    name = 'package'
    allowed_domains = ['openmptcprouter.com']
    start_urls = [
        f'https://packages.openmptcprouter.com/{Version}/aarch64_cortex-a72',
                  f'https://packages.openmptcprouter.com/{Version}/aarch64_cortex-a72/packages',
                  f'https://packages.openmptcprouter.com/{Version}/aarch64_cortex-a72/base',
                  f'https://packages.openmptcprouter.com/{Version}/aarch64_cortex-a72/routing',
                  f'https://packages.openmptcprouter.com/{Version}/aarch64_cortex-a72/telephony',

                  f'https://download.openmptcprouter.com/release/{Version}/rpi4',
                  f'https://download.openmptcprouter.com/release/{Version}/rpi4/packages/aarch64_cortex-a72/base',
                  f'https://download.openmptcprouter.com/release/{Version}/rpi4/packages/aarch64_cortex-a72/luci',
                  f'https://download.openmptcprouter.com/release/{Version}/rpi4/packages/aarch64_cortex-a72/openmptcprouter',
                  f'https://download.openmptcprouter.com/release/{Version}/rpi4/packages/aarch64_cortex-a72/packages'
                  ]

    def parse(self, response: Response):
        trs = response.css('tbody tr')
        for tr in trs:
            item = PackagesItem()

            size = tr.xpath("./td[@class='size']/text()").extract_first()
            link = tr.xpath("./td[@class='link']/a/@href").extract_first()

            item['is_dir'] = size == '-'
            if '../' in link:
                continue

            url = response.url + link
            item['url'] = url
            if item['is_dir']:
                yield scrapy.Request(url, callback=self.parse)
            else:
                yield item








