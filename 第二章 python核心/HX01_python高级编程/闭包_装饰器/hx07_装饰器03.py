# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5

# 在没有修改函数的情况下,对函数的功能进行了扩展

def makeBold(fn):
    print('loading_1')
    def wrapped():
        print('---1---')
        print('b'+fn())
        return '<b>'+fn()+'</b>'
    return wrapped

def makeItalic(fn):
    print('loading_2')
    def wrapped():
        print('---2---')
        print('i'+fn())
        return '<i>'+fn()+'</i>'
    return wrapped

#只要python执行到了这行,就会装饰,即便没有调用函数
@makeBold   # 后装    test = makeBold(test)
@makeItalic  # 先装  test = makeItalic(test)
def test():
    print('---3---')
    return 'hello world-3'

ret = test()
print(ret)