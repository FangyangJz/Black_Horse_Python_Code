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

# 变单任务问题的改进, 把锁放到for里面
# 上锁的地方越少越小越好
# 一旦解锁, 其他线程都在抢
# 等待解锁的方式, 轮询?消息通知?---消息通知效率高!
from threading import Thread,Lock
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        mutex.acquire()  # 如果1方成功上锁, 那么另外一方会堵塞, 直到开锁
        g_num += 1
        mutex.release()

    print('---test1---g_num = %d'%g_num)


def test2():
    global g_num
    for i in range(1000000):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 开锁

    print('---test2---g_num = %d' % g_num)

# 创建一把互斥锁, 默认是开锁状态
mutex = Lock()

t1 = Thread(target=test1)
t1.start()

t2 = Thread(target=test2)
t2.start()