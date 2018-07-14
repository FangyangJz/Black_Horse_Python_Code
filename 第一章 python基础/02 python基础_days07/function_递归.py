# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/13


#代码特点
# 1. 自己调用自己，函数内部的代码是相同的，只是针对参数不同，处理的结果不同（必须有参数）
# 2. 当参数满足一个条件时，函数不再执行 【非常重要，这个叫递归的出口】

def sum_number(num):

    print (num)

    if num == 1:

        return

    sum_number(num-1)
    print ("完成 %d" % num)

sum_number(3)