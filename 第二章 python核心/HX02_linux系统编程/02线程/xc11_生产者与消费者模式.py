# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/3

# 用FIFO(First In First Out)队列实现生产者与消费者问题
# python中的同步队列可以用来 解耦 , 耦合(两个程序关系越紧密越不好)
# 栈stack, LIFO(Last In First Out)

# 进程和线程都可以用生产者与消费者模式来解决双方的速度不匹配的问题

# python2
# from Queue import Queue

# python3
from queue import Queue
# 注意! 这个是 线程 中的Queue,
# 进程 中的队列是 from multiprocessing import Queue

import threading
import time

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(1000):
                    count = count+1
                    msg = '生产者'+str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + '消费者' + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = Queue()

    for i in range(500):
        queue.put('初始产品' + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()