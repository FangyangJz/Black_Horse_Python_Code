# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/3

# GIL 全局解释器锁
# 解决方法一: 用进程, 不用线程

# 线程  有 GIL 控制, 假的多进程, 用单核
# 进程 没有 GIL 控制, 真的多进程, 用了多个核

# 所以,多核时,多进程的效率要远远高于多线程

# 线程间通信 比 进程间通信 便捷

# 解决方法二: 调用C语言写的模块
# 想用线程, 摆脱GIL限制, 用C语言写

from ctypes import *
from threading import Thread

# 加载动态库
lib = cdll.LoadLibrary('./libxxxx.so') # .so文件是gcc xxx.c 编译出来的

# 创建一个子线程, 让其执行C语言编写的函数, 此函数是一个死循环
t = Thread(target=lib.xxxx) # xxxx 是C语言中的函数
t.start()

# 主线程, 也调用C语言编写的那个死循环函数
lib.xxxx()
