# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/3

# 同步就是协同步调, 按预定的先后顺序进行
# 异步, 谁先到了谁先执行, 顺序具有不确定性

# 本例中没有锁就是异步
from threading import Thread, Lock
from time import sleep

class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire(): # 如果lock1能上锁, 就执行if内的语句
                print('----Task 1----')
                sleep(0.5)
                lock2.release()

class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('----Task 2----')
                sleep(0.5)
                lock3.release()

class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('----Task 3----')
                sleep(0.5)
                lock1.release()

lock1 = Lock()
lock2 = Lock()
lock2.acquire()

lock3 = Lock()
lock3.acquire()

t1 = Task1()
t2 = Task2()
t3 = Task3()

t1.start()
t2.start()
t3.start()
