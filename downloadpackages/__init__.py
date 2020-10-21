def start_spider(spider_name):
    from scrapy import cmdline
    cmd = 'scrapy crawl {0}'.format(spider_name)
    print (cmd)
    cmdline.execute(cmd.split())