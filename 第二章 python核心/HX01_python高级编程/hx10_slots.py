# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5

# 如果我们想限制实例的属性,比如只允许Person实例添加name和age属性
# 为了达到限制的目的,Python允许在定义class的时候,定义一个特殊的__slots__变量,
# 来限制该class实例能添加的属性

class Person(object):
    __slots__ = ('name', 'age')

p = Person()
p.name = '老王'
p.age = 30
p.score = 100 # 限制禁止添加
