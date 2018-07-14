# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/2

from threading import Thread
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        g_num += 1

    print('---test1---g_num = %d' % g_num)

def test2():
    global g_num
    for i in range(1000000):
        g_num += 1

    print('---test2---g_num = %d' % g_num)


p1 = Thread(target=test1)
p1.start()

time.sleep(3) # 屏蔽这句就会出现线程共享全局变量的问题, test2的结果不是200万

p2 = Thread(target=test2)
p2.start()

print('---g_num = %d'%g_num)