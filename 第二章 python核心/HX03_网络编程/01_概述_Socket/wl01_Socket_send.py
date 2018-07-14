# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/13


from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
# tcpSocket = socket(AF_INET, SOCK_STREAM)
# 使用 udp 发送的数据,在每一次都需要写上接收方的ip和port
# 在同一个os上,不同程序不能有同一个端口
udpSocket.sendto(b'haha'*10000,('192.168.0.106',7788))




