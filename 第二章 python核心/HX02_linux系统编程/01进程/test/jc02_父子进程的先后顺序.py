# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/30


import os
import time

ret = os.fork()

if ret==0:
    print('---子进程---')
    time.sleep(5)
    print('---子进程over---')
else:
    print('---父进程---')
    time.sleep(3)