# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/12


num = 10


def demo1():

    global num
    # global 声明的全局变量，不会创建局部变量
    num = 99
    print ("demo1 ==> %d" % num)


def demo2():

    print ("demo2 ==> %d" % num)


demo1()
demo2()
