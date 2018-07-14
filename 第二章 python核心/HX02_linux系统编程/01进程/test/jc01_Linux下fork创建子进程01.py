# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/30

# windows 没有fork , win下是multiprocessing模块
import os
import time

ret = os.fork() # 这里会生成一个子进程, 子进程 ret=0, 父进程 ret>0
print(ret)
if ret>0:
    while True:
        print('---1---')
        time.sleep(1)
else:
    while True:
        print('---2---')
        time.sleep(1)
