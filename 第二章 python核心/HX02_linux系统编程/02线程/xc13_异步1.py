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

    # 子进程3s全完事了, 主进程还在睡, 操作系统告诉主进程,
    # 别睡了, 主进程去执行回调函数 (带着你儿子留给你的东西)
    # 子进程返回的 haha 给了操作系统, 操作系统把这个值给了主进程
    time.sleep(5)
    print('---主进程-- pid=%d ---'%os.getpid())
