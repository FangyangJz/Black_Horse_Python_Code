# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/1


from multiprocessing import Manager, Pool
import os, time, random


def reader(q):
    print('reader启动(%s), 父进程为(%s)'%(os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print('reader从Queue获取到消息:%s'%q.get(True))

def writer(q):
    print('writer启动(%s), 父进程为(%s)'%(os.getpid(), os.getppid()))
    for i in 'dongGe':
        q.put(i)


if __name__ == '__main__':
    print('(%s) start' % os.getpid())
    q = Manager().Queue()  # 使用Manager中的Queue来初始化队列
    po = Pool()
    # 使用阻塞模式创建进程, 这样就不需要在reader中使用死循环了,可以让writer执行完成后,在用reader
    po.apply(writer, (q,))
    po.apply(reader, (q,))
    po.close()
    po.join()
    print('(%s) End'%os.getpid())
