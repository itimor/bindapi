# -*- coding: utf-8 -*-
# author: itimor

import requests

node = 'node01'

bind_api_url = 'http://127.0.0.1:8888/api/'
tan_url = 'https://www.tengbo9982.com/favicon.ico'
post_url = bind_api_url + 'domainstatus/'
alldomain_url = bind_api_url + 'getallurls/'

domains = ['www.baidu.com', 'www.taobao.com']  # 实际访问 alldomain_url 获得

for domain in domains:
    html = requests.get(domain, verify=False)

    post_message = {
        'node': node,
        'domain': domain,
    }

    if html.status_code == '200':
        post_message['status'] = True
    else:
        post_message['status'] = False

    requests.post(post_url, data=post_message)
