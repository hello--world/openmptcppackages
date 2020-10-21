#!/data/.envpy3/bin/python3

import os, sys

_srcdir = os.path.dirname(os.path.realpath(__file__))
_filepath = os.path.dirname(sys.argv[0])
sys.path.insert(1, os.path.join(_filepath, _srcdir))

if sys.version_info[0] == 3:
    # import downloadpackages
    from downloadpackages import start_spider
    if __name__ == '__main__':
        start_spider('package')
else: # Python 2
    print("please use python 3")

