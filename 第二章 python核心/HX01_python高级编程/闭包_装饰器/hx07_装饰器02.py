# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5

# 在没有修改函数的情况下,对函数的功能进行了扩展

def w1(func):  #!!!!

    def inner():
        print('checking')

        if True:
            func() # !!!
        else:
            print('没有权限')

    return inner

@w1  # python 语法糖
def f1():
    print('---f1---')

@w1
def f2():
    print('---f2---')

f1()
f2()