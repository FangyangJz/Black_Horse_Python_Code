# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/3


from multiprocessing import Pool
import time
import os

def test():
    print('---进程池中的进程---pid=%d, ppid=%d---'%(os.getpid(), os.getppid()))
    for i in range(3):
        print('---%d---'%i)
        time.sleep(1)
    return 'haha'

def test2(args):
    print('---callback func--pid=%d'%os.getpid())
    print('---callback func--args=%s'%args)

if __name__ == '__main__':

    pool = Pool(3)
    pool.apply_async(func=test, callback=test2)

    # 主进程一直干活, 子进程完成, 主进程放下手中的活去执行callback,
    # 干完callback回来继续执行自己的活
    while True:
        time.sleep(1)
        print('---主进程--pid=%d----'%os.getpid())