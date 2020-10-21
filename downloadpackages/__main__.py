# -*- coding: utf-8 -*-
# """
# 启动爬虫
# """

import sys

# 考虑在这里传参数
def start_spider(spider_name):
    from scrapy import cmdline
    cmd = 'scrapy crawl {0}'.format(spider_name)
    print (cmd)
    cmdline.execute(cmd.split())


def main(argv):
    if len(argv) == 0:
        # usage()
        sys.exit(3)
    try:
        start_spider(argv[1])
    except SystemExit:
        print('exit 0 ~ ')

    else:
        import traceback
        # usage()
        print (traceback.format_exc())
        sys.exit(2)

if __name__ == '__main__':

    main(sys.argv[1:])


