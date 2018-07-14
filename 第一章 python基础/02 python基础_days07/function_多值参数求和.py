# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/13


def sum_numbers(*args):

    num = 0
    print (args)

    for n in args:

        num += n

    return num

result = sum_numbers(1,2,3,4,5)
print result



def sum_numbers_cmp(args): #这里

    num = 0
    print (args)

    for n in args:

        num += n

    return num

result = sum_numbers_cmp((1,2,3,4,5))  #这里
print result
