# -*- coding: utf-8 -*-
# author: itimor

from datetime import timedelta, date
import calendar
import requests


def diff_times_in_seconds(t1, t2):
    h1, m1, s1 = t1.hour, t1.minute, t1.second
    h2, m2, s2 = t2.hour, t2.minute, t2.second
    t1_secs = s1 + 60 * (m1 + 60 * h1)
    t2_secs = s2 + 60 * (m2 + 60 * h2)
    tc = str(timedelta(seconds=(t2_secs - t1_secs)))
    return tc


def getallday(year, smouth, emouth):
    url = 'http://127.0.0.1:9000/api/getpunchs/'
    for mouth in range(smouth, emouth + 1):
        week, monthRange = calendar.monthrange(year, mouth)
        for day in range(1, monthRange + 1):
            sday = date(year, mouth, day).strftime('%Y-%m-%d')
            requests.get(url + sday + '/')
    return

if __name__ == '__main__':
    print(getallday(2018, 1, 3))