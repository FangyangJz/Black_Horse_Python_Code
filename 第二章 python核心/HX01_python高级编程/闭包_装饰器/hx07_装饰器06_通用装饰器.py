# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5

# 在没有修改函数的情况下,对函数的功能进行了扩展


def func(functionName):

    def func_in(*args, **kwargs):
        ret = functionName(*args, **kwargs)
        return ret

    return func_in


@func
def test():
    print('---test---')
    return 'haha'

@func
def test2():
    print('---test2---')

##############################################

@func
def test3(a):
    print('---test3--- a = %d' % a)

ret = test()
print('test return value is %s' % ret)

test2()
print('-'*50)
a = test2()
print(a)

test3(3)