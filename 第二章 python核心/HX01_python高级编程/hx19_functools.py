# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/30

import functools

print(dir(functools))

# 偏函数 functools.partial
print('-'*50)
def showarg(*args, **kwargs):
    print(args)
    print(kwargs)

p1 = functools.partial(showarg, 1,2,3)
# partial 相当于给函数showarg 赋默认的参数
p1()
p1(4,5,6)
print('='*50)
###############################################
# wraps函数
# 下面这个例子, help说明文档时wrapper函数的说明文档
def note(func):
    '''note function'''
    def wrapper():
        '''wrapper function'''
        print('note something')
        return func

    return wrapper

@note
def test():
    '''test function'''
    print('I am test')

print(help(test))
print('='*50)
########################################
# 为了看到test函数的说明文档, 用functools里面的wrapper函数
def note(func):
    '''note function'''
    @functools.wraps(func)
    def wrapper():
        '''wrapper function'''
        print('note something')
        return func

    return wrapper

@note
def test():
    '''test function'''
    print('I am test')

print(help(test))