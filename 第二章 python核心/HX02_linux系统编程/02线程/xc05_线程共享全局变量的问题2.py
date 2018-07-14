# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/2

from threading import Thread
import time

# 不适用time sleep方法
g_num = 0
g_flag = 1 # add

def test1():
    global g_num
    global g_flag #add
    if g_flag == 1:  #add

        for i in range(1000000):
            g_num += 1

        g_flag = 0 #add

    print('---test1---g_num = %d' % g_num)

def test2():
    global g_num
    # 轮询. 一直跑, 直到条件符合才执行然后停止
    while True:
        if g_flag != 1:
            for i in range(1000000):
                g_num += 1
            break #add

    print('---test2---g_num = %d' % g_num)


p1 = Thread(target=test1)
p1.start()

# time.sleep(3) # 屏蔽这句就会出现线程共享全局变量的问题, test2的结果不是200万

p2 = Thread(target=test2)
p2.start()

print('---g_num = %d'%g_num)