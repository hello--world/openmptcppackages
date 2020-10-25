# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

# from itemadapter import ItemAdapter
# import urllib
from urllib import request
from urllib.parse import urlparse

def mkdir(filepath:str):
    path = filepath.split('/')
    path.pop(-1)
    os.makedirs('/'.join(path), exist_ok=True)


class PackagesPipeline:

    def download(self, url):
        o = urlparse(url)
        LocalPath = '/data/openwrtmptcppackages' + o.path
        # os.path.join将多个路径组合后返回
        # urllib.do(url, LocalPath)
        mkdir(LocalPath)
        if not os.path.exists(LocalPath):

            request.urlretrieve(url, LocalPath)

    def process_item(self, item, spider):
        url = item['url']
        self.download(url)

        return item

if __name__ == "__main__":
    # mkdir('/data/ddd/ddd/dd.d')
    # mkdir('/data/ddd/ddd/dd.d')

    p = PackagesPipeline()
    p.download('https://download.openmptcprouter.com/release/v0.55/wrt32x/targets/mvebu/cortexa9/packages/ubi-utils_2.1.1-1_arm_cortex-a9_vfpv3-d16.ipk')

