# -*- coding: utf-8 -*-
# author: itimor

import requests
import json

node = 'node01'

bind_api_url = 'http://118.193.136.206:8000/api/'
tan_page = '/favicon.ico'
post_url = bind_api_url + 'domainstatus/'
alldomain_url = bind_api_url + 'alldomains/'

domains = requests.get(alldomain_url)

for domain in json.loads(domains.text):
    url = 'http://' + domain + tan_page
    html = requests.get(url, verify=False)

    post_message = {
        'node': node,
        'domain': domain,
    }

    if html.status_code == '200':
        post_message['status'] = True
    else:
        post_message['status'] = False

    requests.post(post_url, data=post_message)
