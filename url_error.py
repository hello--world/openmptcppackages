import os
import urllib
from urllib.parse import urlencode

from urllib.parse import unquote

g = os.walk("/data/openwrtmptcppackages")
#
# for path,dir_list,file_list in g:
#     for dir_name in dir_list:
#         print(os.path.join(path, dir_name) )


for path,dir_list,file_list in g:
    for file_name in file_list:
        url_path = os.path.join(path, file_name)
        new_path = unquote(url_path, 'utf-8')
        if url_path != new_path:

            print(url_path, new_path)
            os.system(f"mv \"{url_path}\"  \"{new_path}\" ")