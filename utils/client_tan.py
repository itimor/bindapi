# -*- coding: utf-8 -*-
# author: itimor

import requests
import json
import time
import threading
import sys

if sys.version_info < (3, 4):
    from Queue import Queue
else:
    from queue import Queue


class ThreadUrl(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        pass


class Tan(object):
    def __init__(self, node, tan_page):
        self.node = node
        self.bind_api_url = 'http://118.193.136.206:8000/api/'
        self.tan_page = tan_page
        self.tanpost_uri = 'domainstatus/'
        self.alldomain_uri = 'alldomains/'

    def get_domains(self):
        req = requests.get(self.bind_api_url + self.alldomain_uri)
        return json.loads(req.text)


if __name__ == '__main__':
    node = 'node01'
    tan_page = '/favicon.ico'
    tan = Tan(node, tan_page)
    domains = tan.get_domains()

    threads = []
    for domain in domains:
        url = 'http://' + domain + tan.tan_page
        html = requests.get(url, verify=False)

        post_message = {
            'node': node,
            'domain': domain,
        }

        if html.status_code == '200':
            post_message['status'] = True
        else:
            post_message['status'] = False

        # requests.post(tan.bind_api_url + tan.tanpost_uri, data=post_message)
        t = threading.Thread(target=requests.post(tan.bind_api_url + tan.tanpost_uri, data=post_message))
        threads.append(t)

        time.sleep(20)
        for thr in threads:
            thr.start()