# -*- coding: utf-8 -*-
# author: itimor

import re
import requests


class SeBook(object):
    def __init__(self, main_url, total_page_comp, page_url_comp, title_page_comp, keyword_comp):
        self.main_url = main_url
        self.total_page_comp = total_page_comp
        self.page_url_comp = page_url_comp
        self.title_page_comp = title_page_comp
        self.keyword_comp = keyword_comp

    def encode_char(self, url):
        html = requests.get(url)
        html.encoding = 'GB2312'
        return html.text

    def comp_match(self, d):
        r = re.findall(self.keyword_comp, d)
        if len(r) > 0:
            return True
        else:
            return False

    def main(self):
        list_data = self.encode_char(self.main_url)
        total_page = int(re.findall(self.total_page_comp, list_data)[0])
        page_url = re.findall(self.page_url_comp, list_data)[0]

        # get all_page_urls
        page_urls = []
        for i in range(1, total_page):
            if i == 1:
                page_urls.append(self.main_url + 'index.html')
            else:
                page_urls.append(self.main_url + page_url + str(i) + '.html')

        # get_all_title_pageurl
        re_list = []
        for page in page_urls:
            title_list = self.encode_char(page)
            d = re.findall(self.title_page_comp, title_list)
            for item in d:
                if self.comp_match(item[1]) and item not in re_list:
                    # with open('yuse.txt', 'w') as fn:
                    #     fn.write('{} {}{}'.format(item[1], url, item[0]))
                    re_list.append(self.main_url + item[0])

        return re_list


if __name__ == '__main__':
    main_url = 'http://www.yusetv.com/wenxue/renqiluanlun/'
    total_page_comp = re.compile(r"_\d+_(\d+).html'>末页")
    page_url_comp = re.compile(r"'(list_\d+_)\d+.html'>末页")
    title_page_comp = re.compile(r'<i>\d+-\d+-\d+</i><a href="/wenxue/renqiluanlun/(\d+/\d+.html)">\[(.*?)\]')
    keyword_comp = re.compile(r'.*[姐|妹|哥|姊].*')
    # keyword_comp = re.compile(r'.*[姐|妹|师|姊|花]!奸.*')
    sebook = SeBook(main_url, total_page_comp, page_url_comp, title_page_comp, keyword_comp)
    print(sebook.main())
