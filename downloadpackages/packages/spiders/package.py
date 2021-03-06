import scrapy
from scrapy.http import Response
from downloadpackages.packages.items import PackagesItem
from downloadpackages.log import log
# from scrapy_redis.spiders import RedisSpider

class PackageSpider(scrapy.Spider):
    name = 'package'
    allowed_domains = ['openmptcprouter.com']
    start_urls = ['http://packages.openmptcprouter.com/v0.56.5/aarch64_cortex-a72/luci',
                  'http://packages.openmptcprouter.com/v0.56.5/aarch64_cortex-a72/packages',
                  'http://packages.openmptcprouter.com/v0.56.5/aarch64_cortex-a72/base',
                  'http://packages.openmptcprouter.com/v0.56.5/aarch64_cortex-a72/routing',
                  'http://packages.openmptcprouter.com/v0.56.5/aarch64_cortex-a72/telephony',

                  'http://download.openmptcprouter.com:80/release/v0.56.5/rpi4/targets/bcm27xx/bcm2711/packages',
                  'http://download.openmptcprouter.com:80/release/v0.56.5/rpi4/packages/aarch64_cortex-a72/base',
                  'http://download.openmptcprouter.com:80/release/v0.56.5/rpi4/packages/aarch64_cortex-a72/luci',
                  'http://download.openmptcprouter.com:80/release/v0.56.5/rpi4/packages/aarch64_cortex-a72/openmptcprouter',
                  'http://download.openmptcprouter.com:80/release/v0.56.5/rpi4/packages/aarch64_cortex-a72/packages'
                  ]

    def parse(self, response: Response):

        all_link = response.xpath('//a/@href')
        links = []
        for link in all_link:
            url = link.extract()
            url = response.url + url
            links.append(url)
            log.info(url)

        is_dirs = []
        all_text = response.xpath('/html/body/pre/text()')
        for _text in all_text:
            text: str = _text.extract()
            text = text.strip()
            laststr = text.split(' ')[-1]
            print("-->" + laststr + "<--")
            is_dirs.append(laststr=='-')

        for i in range(len(all_link)):
            item = PackagesItem()
            url = links[i]
            if '../' in url:
                continue
            is_dir = is_dirs[i]
            item['url'] = url
            item['is_dir'] = is_dir

            if is_dir:
                yield scrapy.Request(url, callback=self.parse)
            else:
                yield item







