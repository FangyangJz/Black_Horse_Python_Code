# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/3


import threading
import time

# 除了这里介绍的方法(添加超时时间),
# 还有一个:在设计程序的时候要尽量避免银行家算法

class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name+'---do1--up---')
            time.sleep(1)

            if mutexB.acquire():
                print(self.name+'---do1---down----')
                mutexB.release()
            mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        if mutexB.acquire(): # 注意这里面的参数blocking和timeout
            print(self.name + '---do2--up---')
            time.sleep(1)

            if mutexA.acquire(timeout=2): # 此处解决死锁的问题, 是加超时时间(看门狗)
                # 过了2秒不解锁, 就继续往下走, 不等在这
                print(self.name + '---do2---down----')
                mutexA.release()
            mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()

