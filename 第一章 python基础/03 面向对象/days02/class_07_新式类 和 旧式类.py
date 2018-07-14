# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/3


# object 是 python 为所有对象提供的 基类，提供有一些内置的属性和方法，可以使用dir函数查看
# 新式类 ： 以object为基类的类，推荐使用
# 经典类 ： 不以object为该类的基类（python 3 中定义的类，如果没有指定父类，会默认使用object作
# 为基类）



# ipython中运行

class A(object):
    pass
a = A()
dir(a)

    # Out[4]:
    # ['__class__',
    #  '__delattr__',
    #  '__dict__',
    #  '__doc__',
    #  '__format__',
    #  '__getattribute__',
    #  '__hash__',
    #  '__init__',
    #  '__module__',
    #  '__new__',
    #  '__reduce__',
    #  '__reduce_ex__',
    #  '__repr__',
    #  '__setattr__',
    #  '__sizeof__',
    #  '__str__',
    #  '__subclasshook__',
    #  '__weakref__']

class B:
    pass
b = B()
dir(b)

    # Out[7]: ['__doc__', '__module__']
