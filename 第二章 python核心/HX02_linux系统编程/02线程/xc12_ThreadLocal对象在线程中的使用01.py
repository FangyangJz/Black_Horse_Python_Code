# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/3

# 使用全局字典方式

import threading
# import time

globals_dict = {}

def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中
    globals_dict[threading.current_thread().name] = std
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std, 而是根据当前线程查找
    std = globals_dict[threading.current_thread().name]

def do_task_2():
    # 不传入std, 而是根据当前线程查找
    std = globals_dict[threading.current_thread().name]