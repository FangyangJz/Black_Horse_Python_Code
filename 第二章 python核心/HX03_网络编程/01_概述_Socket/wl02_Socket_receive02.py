# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/13

from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(('', 7788))
recvData = udpSocket.recvfrom(1024)
print(recvData)
print(recvData[0].decode('utf-8'))
# print(recvData[0].decode('gbk'))
content,destinfo = recvData
print('content is %s' % content.decode('utf-8'))
print(destinfo) 
