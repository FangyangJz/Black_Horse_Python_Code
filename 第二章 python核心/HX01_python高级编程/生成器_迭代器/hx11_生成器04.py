# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5


def test1():
    while True:
        print('---1---')
        yield None

def test2():
    while True:
        print('---2---')
        yield None

t1 = test1()
t2 = test2()
while True:
    t1.__next__()
    t2.__next__()

# 多任务(协程, 01进程, 02线程),此处是协程, 看上去在同时执行