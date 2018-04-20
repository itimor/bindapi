# -*- coding: utf-8 -*-
# author: itimor

import re
import requests


def encode_char(url):
    html = requests.get(url)
    html.encoding = 'GB2312'
    return html.text


def comp(m, d):
    r = re.findall(m, d)
    if len(r) > 0:
        return True
    else:
        return False


m = re.compile(r'.*[姐|妹|哥|姊].*')

url = 'http://www.yusetv.com/wenxue/renqiluanlun/'
data = encode_char(url)
total_page = int(re.findall("_\d+_(\d+).html'>末页", data)[0])
page_url = re.findall("'(list_\d+_)\d+.html'>末页", data)[0]

title_page = re.compile(r'<i>\d+-\d+-\d+</i><a href="/wenxue/renqiluanlun/(\d+/\d+.html)">\[(.*?)\]')

# get all_page_urls
page_urls = []
for i in range(1, total_page):
    if i == 1:
        page_urls.append(url + 'index.html')
    else:
        page_urls.append(url + page_url + str(i) + '.html')

re_list = []
for page in page_urls:
    title_list = encode_char(page)
    d = re.findall(title_page, title_list)
    for item in d:
        if comp(m, item[1]) and item not in re_list:
            re_list.append(url + item[0])

print(re_list)
