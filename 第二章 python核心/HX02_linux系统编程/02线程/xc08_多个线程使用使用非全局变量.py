# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/3


from threading import Lock, Thread, current_thread
import time

# 非全局变量, 不用加锁

def test1():
    name = current_thread().name
    print('---thread name is %s ---'%name)
    g_num = 100
    if name == 'Thread-1':
        g_num += 1
    else:
        time.sleep(2)
    print('---thread is %s---g_num=%d' % (name, g_num))

# def test2():
#     g_num = 100
#     g_num += 1
#     print('---test2---g_num=%d'%g_num)

t1 = Thread(target=test1)
t1.start()

t2 = Thread(target=test1)
t2.start()

# print('---g_num=%d---'%g_num)

