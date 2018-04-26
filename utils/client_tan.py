# -*- coding: utf-8 -*-
# author: itimor

import requests
import json
import threading
import sys

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if sys.version_info < (3, 4):
    from Queue import Queue, Empty
else:
    from queue import Queue, Empty


class TanThread(threading.Thread):
    def __init__(self, thread_name, domains_queue, node, tanpost_url):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.domains_queue = domains_queue
        self.node = node
        self.tanpost_url = tanpost_url
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print("thread %s: waiting for task" % self.thread_name)
            try:
                domain = self.domains_queue.get(block=True, timeout=5)
                print("task https://%s is running" % domain)
                post_data(domain, self.node, self.tanpost_url)
            except Empty:
                print("Nothing to do! to play ball!")
                self.thread_stop = True
                break
        self.domains_queue.task_done()

    def stop(self):
        self.thread_stop = True


def get_domains(alldomain_url):
    req = requests.get(alldomain_url)
    return json.loads(req.text)


def post_data(domain, node, tanpost_url):
    url = 'http://' + domain + tan_page
    post_message = {
        'node': node,
        'domain': domain,
    }
    try:
        html = requests.get(url, verify=False)
        if html.status_code == '200':
            post_message['status'] = True
        else:
            post_message['status'] = False
    except Exception as e:
        post_message['status'] = False

    requests.post(tanpost_url, data=post_message)


def main(node):
    tanpost_url = 'http://118.193.136.206:8000/api/domainstatus/'
    alldomain_url = 'http://118.193.136.206:8000/api/alldomains/'

    domains = get_domains(alldomain_url)

    domains_queue = Queue()

    for domain in domains:
        domains_queue.put(domain)

    threads = []
    thread_list = ['xxoo-01', 'xxoo-02', 'xxoo-03', 'xxoo-04', 'xxoo-05']
    for thread_name in thread_list:
        t = TanThread(thread_name, domains_queue, node, tanpost_url)
        t.setDaemon(True)
        t.start()
        threads.append(t)

    # 等待队列清空
    while not domains_queue.empty():
        pass

    # 等待所有线程完成
    for t in threads:
        t.join()


if __name__ == '__main__':
    node = 'node01'
    tan_page = '/favicon.ico'
    main(node)
