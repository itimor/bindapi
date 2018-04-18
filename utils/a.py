# -*- coding: utf-8 -*-
# author: itimor

import requests
import json
from dns.resolver import query


def dnsinfo(url, type):
    try:
        info = query(url, type)
        for i in info.response.answer:
            for j in i.items:
                result = j.to_text()
        return result
    except:
        return ''


def diffdns(allurl):
    allurls = json.loads(requests.get(allurl).text)
    oo = []
    for url in allurls:
        uu = 'http://127.0.0.1:8888/api/domainstatus/?url='
        urlinfos = json.loads(requests.get(uu + url['url']).text)
        c = dict()
        for info in urlinfos:
            c[info['node']] = info['ip']
        ss = []
        ee = []
        all = len(urlinfos)
        ainfo = url['value']
        for info in urlinfos:
            if info['ip'] == ainfo:
                ss.append(info['node'])
            else:
                ee.append(info['node'])
        dinfo = dict()
        if len(ss) > all/2:
            dinfo['status'] = 'true'
            a = []
            for h in ss:
                a.append(c[h])
            dinfo['value'] = list(set(a))
        else:
            dinfo['status'] = 'false'
            b = []
            for h in ee:
                b.append(c[h])
            dinfo['value'] = list(set(b))
        oo.append({url['url']: dinfo})
    return oo


if __name__ == '__main__':
    allurl = 'http://127.0.0.1:8888/api/getallurls/'
    print(diffdns(allurl))
