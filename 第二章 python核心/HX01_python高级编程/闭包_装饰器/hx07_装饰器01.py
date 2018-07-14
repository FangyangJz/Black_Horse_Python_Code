# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5

# 在没有修改函数的情况下,对函数的功能进行了扩展

def test1():
    print('---1---')

def test1():
    print('---2---')

test1()

#######################################

def w1(func):  #!!!!
    def inner():
        print('checking')
        func() # !!!
    return inner

def f1():
    print('---f1---')

def f2():
    print('---f2---')

# innerfunc = w1(f1)
# innerfunc()

f1 = w1(f1)
f1()