# -*- coding: utf-8 -*-
# author: itimor

from win32com.client import Dispatch
from zkconf import ZK_INFO

# 设置信息
m_id = 2
zk = Dispatch("zkemkeeper.ZKEM")
zk.Connect_Net(ZK_INFO['HOST'], ZK_INFO['PORT'])

# 注册全部实时事件
zk.RegEvent(m_id, 65535)


class ZKAPI(object):
    def __init__(self, m_id, zk):
        self.m_id = m_id
        self.zk = zk

    def getReadAllGLogData(self):
        """
        获取所有签到数据
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
        if self.zk.ReadGeneralLogData(self.m_id):
            alldatas = []
            while True:
                data = self.zk.SSR_GetGeneralLogData(self.m_id)
                rdata = dict()
                if data[0]:
                    rdata['is_punch'] = data[0]
                    rdata['user_id'] = data[1]
                    rdata['EnrollNumber'] = data[2]
                    rdata['verifymode'] = data[3]
                    rdata['create_time'] = '{}-{}-{} {}:{}:{}'.format(data[4], data[5], data[6], data[7], data[8],
                                                                      data[9])
                    rdata['desc'] = data[10]
                    alldatas.append(rdata)
                else:
                    break
            return alldatas

    def getAllUserInfo(self):
        """
        读取所有的用户信息
        :return:
            True， 有数据，
            1，EnrollNumber/用户编号
            '***', Password/用户密码
            'aaa',Name/用户姓名
            '114',卡号
            True，Enabled/用户启用
        """
        if self.zk.GetAllUserInfo(self.m_id):
            alldatas = []
            while True:
                data = self.zk.GetAllUserInfo(self.m_id)
                rdata = dict()
                if data[0]:
                    rdata['is_punch'] = data[0]
                    rdata['user_id'] = data[1]
                    rdata['password'] = data[2]
                    rdata['username'] = data[3]
                    rdata['card_id'] = data[4]
                    rdata['is_active'] = data[5]
                    alldatas.append(data)
                else:
                    break
            return alldatas

    def getUserInfo(self, user_id):
        """
        读取所有的用户信息
        :return:
            True， 有数据，
            'aaa',Name/用户姓名
            '***', Password/用户密码
            '114',卡号
            True，Enabled/用户启用
        """
        data = self.zk.SSR_GetUserInfo(self.m_id, user_id)
        return data


if __name__ == '__main__':
    zkapi = ZKAPI(m_id, zk)
    print(zkapi.getUserInfo(1002))
