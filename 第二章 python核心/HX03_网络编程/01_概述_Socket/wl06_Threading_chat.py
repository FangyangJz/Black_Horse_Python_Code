# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/13


from threading import Thread
from socket import *


# 1. 收数据,然后打印
def recvData():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print('>>%s:%s'%(str(recvInfo[1]), recvInfo[0]))

# 2. 检测键盘,发数据
def sendData():
    while True:
        sendInfo = input('<<')
        udpSocket.sendto(sendInfo.encode('utf-8'), (destIP,destPort))

udpSocket = None
destIP = ''
destPort = 0

def main():

    global udpSocket
    global destIP
    global destPort

    destIP = input('对方的IP:')
    destPort = input('对方的Port:')

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.close()
    # udpSocket.bind(('', 45675))

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == '__main__':
    main()