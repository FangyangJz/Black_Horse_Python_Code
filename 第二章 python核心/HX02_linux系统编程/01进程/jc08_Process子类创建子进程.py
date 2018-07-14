# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/31

# 当一个函数无法满足子进程需求的时候, 这是后需要一个类
# 这个类要继承Process类

from multiprocessing import Process
import time
import os

class Process_Class(Process):

    def __init__(self, interval):
    # '''因为Process类本身有__init__方法, 所以这里为了防止重写覆盖,'''
    # 将继承类本身传递给Process.__init__方法
        Process.__init__(self)
        self.interval = interval

    def run(self):
    # 重写run()方法, start后一定会调用run方法
        print('子进程(%s)开始执行, 父进程为(%s)'%(os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print('(%s)执行结果, 耗时%0.2f秒'%(os.getpid(), (t_stop - t_start)))

if __name__ == '__main__':
    t_start = time.time()
    print('当前程序进程(%s)' % os.getpid())
    p1 = Process_Class(2)
    p1.start()
    p1.join()
