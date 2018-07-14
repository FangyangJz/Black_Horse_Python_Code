# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/31

import os

ret = os.fork()
if ret == 0:
    print('--1--')
else:
    print('--2--')


ret = os.fork()
if ret == 0:
    print('--11--')
else:
    print('--22--')