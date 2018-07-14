# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/31


from multiprocessing import Queue, Process
import os, time, random


def write(q):
    '''写数据进程执行的代码'''
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    '''读数据进程执行的代码'''
    while True:

        if not q.empty():
            value = q.get()
            print('Get %s from queue...' % value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    # 父进程创建Queue, 并传给各个子进程
    q = Queue()

    pw = Process(target=write, args=(q,))
    # 这里必须要有target= ,否则报下面的错
    # AssertionError: group argument must be None for now
    pr = Process(target=read, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
