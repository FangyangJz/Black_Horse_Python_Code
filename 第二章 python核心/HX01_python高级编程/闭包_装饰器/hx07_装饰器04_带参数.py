# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5

# 在没有修改函数的情况下,对函数的功能进行了扩展


def outer(funcName):

    print('---outer----1--')

    def inner(aa, bb): #  *argv, **kwargv
        print('---inner---1---')
        funcName(aa, bb)   #  *argv, **kwargv
        print('---inner---2---')

    print('---outer---2---')

    return inner

@outer
def test(a, b):
    print('---test--a=%d, b=%d----'%(a, b))

test(11,22)