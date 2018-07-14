# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/30

import os

ret = os.fork()
print(ret) # ret是创建出来的子进程

if ret>0:
    print('---父进程---%d---'%os.getpid())
else:
    # getppid()获取的是父进程的pid
    print('---子进程---%d-%d-'%(os.getpid(), os.getppid()))