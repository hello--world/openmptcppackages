# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

# from itemadapter import ItemAdapter
# import urllib
from urllib import request
from urllib.parse import urlparse, unquote


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
            try:
                new_path = unquote(LocalPath, 'utf-8')

                request.urlretrieve(url, new_path)
                print(f"download {url}")
            except:
                print(f"download error {url}")


    def process_item(self, item, spider):
        url = item['url']
        self.download(url)

        return item

if __name__ == "__main__":
    mkdir('/data/ddd/ddd/dd.d')
    mkdir('/data/ddd/ddd/dd.d')

