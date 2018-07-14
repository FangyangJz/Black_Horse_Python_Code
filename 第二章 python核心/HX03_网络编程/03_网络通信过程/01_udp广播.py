# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/12


# '''
# udp可以广播, tcp不行
# '''

import socket, sys

# 192.168.0.255 , 255是广播, 但是如果我不在.0, 那么还是下面这种写法好
dest = ('<broadcast>', 80)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 对这个需要发送广播数据的套接字进行修改设置, 否则不能发送广播数据
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.sendto(0b0111, dest)


