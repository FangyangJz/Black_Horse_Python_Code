# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/31

from multiprocessing import Process
import os
import time

def test():
    while True:
        print('---test---')
        time.sleep(1)

if __name__ == '__main__':

    p = Process(target=test)
    p.start() # 让这个进程执行test函数中的代码

    while True:
        print('---main---')
        time.sleep(1)