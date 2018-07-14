# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/12

# 在开发时，应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证所有的函数都能正常访问每一个局部变量了

num = 10
title = '黑马程序员'
name = "小明"


def demo():

    print ("%d" % num)
    print ("%s" % title)
    print ("%s" % name)


demo()

