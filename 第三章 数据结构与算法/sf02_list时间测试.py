# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/2

from timeit import Timer

# 构造列表的几种方式
# li1=[1,2]
# li2=[3,5]
# li = li1+li2
# ###################################
# li = [i for i in range(10000)]
# ###################################
# li = list(range(10000))
# ##################################
# li = []
# for i in range(10000):
#     li.append(i)
# ####################################

def test1():
    li = []
    for i in range(10000):
        li.append(i)

def test2():
    li = []
    for i in range(10000):
        li += [i]
        # 换成 li = li+[i] 后时间复杂度飙升,速度200+秒
        # li += [i] 其实相当于 li.extend([i])

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))

def test5():
    li = []
    for i in range(10000):
        li.extend([i])

timer1 = Timer('test1()','from __main__ import test1')
print('append:',timer1.timeit(1000))

timer1 = Timer('test2()','from __main__ import test2')
print('+:',timer1.timeit(1000))

timer1 = Timer('test3()','from __main__ import test3')
print('[i for i in range]',timer1.timeit(1000))

timer1 = Timer('test4()','from __main__ import test4')
print('list(range())',timer1.timeit(1000))

timer1 = Timer('test5()','from __main__ import test5')
print('extend([])',timer1.timeit(1000))