# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/31

# 当需要创建的子进程数量不多时, 可以直接利用multiprocessing中的Process动态生成
# 多个子进程, 但如果是成百上千个目标, 手动创建工作量巨大, 此时可以用multiprocessing模块
# 提供的Pool方法

from multiprocessing import Pool
import os, time, random


def worker(num):
    for i in range(random.randint(1,3)):
        print('----pid = %d --num=%d--' % (os.getpid(),num))
        time.sleep(1)

if __name__ == '__main__':

    pool = Pool(3) # 定义一个进程池, 最大进程数为3
    # 用 po.apply_async(func, (args,), kwds=) 来向进程池里面添加进程
    for i in range(10):
        print('---%d---'%i)
        pool.apply_async(worker,(i,))

    pool.close() # 关闭进程池, 关闭后pool不再添加新的任务
    pool.join() # 等待pool中所有子进程执行完成, 必须放在close语句之后
    # 如果没有join , 会导致进程池中的任务不会执行
    print('end')