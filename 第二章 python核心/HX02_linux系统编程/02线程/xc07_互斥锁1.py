# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/2

# xc05_线程共享全局变量的问题2 中引入轮询概念
# 轮询效率不高, 这里就考虑用互斥锁

# 创建锁
# mutex = threading.Lock()
# # 锁定
# mutex.acquire([blocking])
# # 释放
# mutex.release()

# 本程序用互斥锁改写后, 变成了单任务执行啊!!!
from threading import Thread,Lock
import time

g_num = 0

def test1():
    global g_num
    mutex.acquire() # 如果1方成功上锁, 那么另外一方会堵塞, 直到开锁

    for i in range(1000000):
        g_num += 1

    mutex.release()
    print('---test1---g_num = %d'%g_num)


def test2():
    global g_num
    mutex.acquire() # 上锁

    for i in range(1000000):
        g_num += 1

    mutex.release() # 开锁
    print('---test2---g_num = %d' % g_num)

# 创建一把互斥锁, 默认是开锁状态
mutex = Lock()

t1 = Thread(target=test1)
t1.start()

t2 = Thread(target=test2)
t2.start()