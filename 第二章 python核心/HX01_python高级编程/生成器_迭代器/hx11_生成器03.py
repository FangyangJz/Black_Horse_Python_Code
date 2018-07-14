# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5


# 可以有多个yield,但是执行都是从上一次的yield开始

def test():
    i = 0
    while i < 5:
        if i == 0:
            temp = yield i
            print(temp)
        else:
            yield i
        i += 1

t = test()
t.__next__()
t.send('haha')



