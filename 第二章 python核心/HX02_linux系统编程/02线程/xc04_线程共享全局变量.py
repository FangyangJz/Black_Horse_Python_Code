# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/2


from threading import Thread
import time

g_num = 100

def work1():
    global g_num # 在函数中想使用全局变量, 同时对其做修改
    for i in range(3):
        g_num += 1

    print('---in work1, g_num is %d' % g_num)

def work2():
    global g_num
    print('---in work2, g_num is %d' % g_num)

print('---线程创建前g_num is %d' % g_num)
t1 = Thread(target=work1)
t1.start()
# 延迟一会, 保证t1线程中的事情做完
time.sleep(1)

# 进程不会共享全局变量(除了进程间通信了),
# 线程之间共享全局变量(他们在同一个进程中), 这是进程和线程的区别!!!
t2 = Thread(target=work2)
t2.start()
