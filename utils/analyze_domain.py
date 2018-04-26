# -*- coding: utf-8 -*-
# author: itimor

import requests
import json


def diffdns(alldomains):
    domains = json.loads(requests.get(alldomains).text)
    oo = []
    for domain in domains:
        uu = 'http://118.193.136.206:8000/api/domainstatus/?domain='
        urlinfos = json.loads(requests.get(uu + domain).text)
        ss = []
        ee = []
        for info in urlinfos:
            if info['status']:
                ss.append(info['node'])
            else:
                ee.append(info['node'])
        result = dict()
        result['node_count'] = len(urlinfos)
        result['error_node'] = ee
        result['url'] = domain

        if len(ss) > result['node_count'] / 2:
            result['status'] = True
        else:
            result['status'] = False

        oo.append(result)
    return oo


if __name__ == '__main__':
    alldomains = 'http://118.193.136.206:8000/api/alldomains/'
    print(diffdns(alldomains))
