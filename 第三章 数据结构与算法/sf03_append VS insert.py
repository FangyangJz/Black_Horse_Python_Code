# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/2

from timeit import Timer

def t1():
    li = []
    for i in range(10000):
        li.append(i)

def t2():
    li = []
    for i in range(10000):
        li.insert(0, i)
        # 这里用0表示插入到队头,速度38s; 换成-1表示插队尾,速度快了,1.87s

timer = Timer('t1()', 'from __main__ import t1')
print('append', timer.timeit(1000))

timer = Timer('t2()', 'from __main__ import t2')
print('insert', timer.timeit(1000))

# append 0.9636843270227156
# insert 38.07776773884107  向队头添加列表

# 课件中还测试了pop_zero和pop_end
# 从队头pop_zero 速度1.9s
# 从队尾pop_end  速度0.0002s