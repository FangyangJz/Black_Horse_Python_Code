# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/13


from socket import *

def main():

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('', 7788))
    num = 1

    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print('[%s]:%s' % ((str(recvInfo[1])), recvInfo[0].decode('utf-8')))

        # 这里开始 echo 返回信息
        udpSocket.sendto(recvInfo[0],recvInfo[1])
        # 统计信息
        print('已经将接收到的第%d个数据返回给对方,内容为:%s' % (num, recvInfo[0]))
        num += 1

    udpSocket.close()


if __name__ == '__main__' :
    main()
