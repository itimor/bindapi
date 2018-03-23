# -*- coding: utf-8 -*-
# author: itimor

from win32com.client import Dispatch
from zkconf import ZK_INFO

m_id = 2
zk = Dispatch("zkemkeeper.ZKEM")
zk.Connect_Net(ZK_INFO['HOST'], ZK_INFO['PORT'])

# 注册全部实时事件
zk.RegEvent(m_id, 65535)


def getReadAllGLogData(m_id):
    """
    获取所有签到数据
    :param m_id: 2
    :return:
        True， 有数据，
        u'x' , 用户id
        1，EnrollNumber
        255,verifymode
        2015, 年份
        12，月份
        21，日期
        16， 时
        14，分
        37，秒
        0，备用码
    """
    if zk.ReadGeneralLogData(m_id):
        alllogdatas = []
        while True:
            data = zk.SSR_GetGeneralLogData(m_id)
            logdata = dict()
            if data[0]:
                logdata['is_punch'] = data[0]
                logdata['user_id'] = data[1]
                logdata['EnrollNumber'] = data[2]
                logdata['verifymode'] = data[3]
                logdata['create_time'] = '{}-{}-{} {}:{}:{}'.format(data[4], data[5], data[6], data[7], data[8],
                                                                    data[9])
                logdata['desc'] = data[10]
                alllogdatas.append(logdata)
            else:
                break
        return alllogdatas

    if __name__ == '__main__':
        print(getReadAllGLogData(2))
