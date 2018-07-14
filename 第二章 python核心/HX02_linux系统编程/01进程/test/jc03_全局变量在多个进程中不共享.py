# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/31

# 全局变量在进程间不共享, 要想共享, 后面学
import os
import time

g_num = 100

ret = os.fork()
if ret == 0:
    print('---process1---')
    g_num += 1
    print('---process_1  g_num=%d---'%g_num)

else:
    time.sleep(3)
    print('---process2---')
    print('---process_2  g_num=%d---'%g_num)