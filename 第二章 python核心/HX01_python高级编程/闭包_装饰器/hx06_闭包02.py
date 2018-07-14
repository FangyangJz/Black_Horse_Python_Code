# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5


def line_conf(a,b):

    def line(x):
        return a*x + b

    return line

line1 = line_conf(1,1)
line2 = line_conf(4,5)
print(line1(5))
print(line2(5))