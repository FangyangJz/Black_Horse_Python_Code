# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/13


from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

destIP = '192.168.0.106'
destPort = 7788
flag = True

while flag:
    sendData =input('[退出程序输入q回车]请输入要发送的data: ')
    if sendData == 'q':
        flag = False
        break
    udpSocket.sendto(sendData.encode('utf-8'),(destIP,destPort))
    # 不加encode(str='utf-8), 得在发送的字符串前加b
    recvData = udpSocket.recvfrom(1024)
    print(recvData)