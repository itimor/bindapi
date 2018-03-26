# -*- coding: utf-8 -*-
# author: itimor

from zkapi.settings import zk
from zkapi.settings import zk_m_id as m_id
from datetime import datetime, date, time


def getReadAllGLogData():
    """
    获取所有签到数据
    :return:
        True， 有数据，
        1005: EnrollNumber/用户号
        1,verifymode/0 为密码验证，1 为指纹验证，2 为卡验证
        255, 未知
        2015, 年份/ 12，月份/ 21，日期/ 16， 时/ 14，分/ 37，秒
        0，备用码
    """
    if zk.ReadGeneralLogData(m_id):
        alldatas = []
        while True:
            data = zk.SSR_GetGeneralLogData(m_id)
            rdata = dict()
            if data[0] and data[4]:
                cur_date = datetime.now().strftime('%Y-%m-%d')
                create_datetime = datetime(data[4], data[5], data[6], data[7], data[8], data[9])
                create_date = date(data[4], data[5], data[6]).strftime('%Y-%m-%d')
                create_time = time(data[7], data[8], data[9])
                if cur_date == create_date:
                    rdata['user_id'] = data[1]
                    rdata['verifymode'] = data[2]
                    rdata['create_datetime'] = create_datetime
                    rdata['create_date'] = create_date
                    rdata['create_time'] = create_time
                    alldatas.append(rdata)
            else:
                break
        return alldatas


def getAllUserInfo():
    """
    读取所有的用户信息
    :return:
        True， 有数据，
        1，EnrollNumber/用户号
        'aaa',Name/用户姓名
        '***', Password/用户密码
        '0',Privileg/用户权限，3 为管理员，0 为普通用户
        True，Enabled/用户启用
    """
    if zk.ReadAllUserID(m_id):
        alldatas = []
        while True:
            data = zk.SSR_GetAllUserInfo(m_id)
            rdata = dict()
            if data[0]:
                rdata['user_id'] = data[1]
                rdata['username'] = data[2]
                rdata['password'] = data[3]
                rdata['role'] = data[4]
                rdata['is_active'] = data[5]
                alldatas.append(rdata)
            else:
                break
        return alldatas


if __name__ == '__main__':
    print(getAllUserInfo())
    zk.Disconnect()
