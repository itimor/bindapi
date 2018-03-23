# -*- coding: utf-8 -*-
# author: itimor

from win32com.client import Dispatch
import sys
from zkconf import ZK_INFO

m_id = 2
zk = Dispatch("zkemkeeper.ZKEM")

if not zk.Connect_Net(ZK_INFO['HOST'], ZK_INFO['PORT']):
    print("考勤机连接错误")
    sys.exit(1)

zk.RegEvent(m_id, 65535)

print("获取所有签到数据")
if zk.ReadGeneralLogData(m_id):
    while True:
        data = zk.SSR_GetGeneralLogData(m_id)
        if data[0]:
            print(data)
        else:
            break
zk.EnableDevice(m_id, True)  # enable the device
zk.Disconnect()

"""
# 结果说明：
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
