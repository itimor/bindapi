# -*- coding: utf-8 -*-
# author: itimor

import requests
import json


def diffdns(allurl):
    allurls = json.loads(requests.get(allurl).text)
    oo = []
    for url in allurls:
        uu = 'http://127.0.0.1:8888/api/domainstatus/?domain='
        urlinfos = json.loads(requests.get(uu + url).text)
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
        result['url'] = url

        if len(ss) > result['node_count']/2:
            result['status'] = True
        else:
            result['status'] = False

        oo.append(result)
    return oo


if __name__ == '__main__':
    allurl = 'http://127.0.0.1:8888/api/getallurls/'
    print(diffdns(allurl))
