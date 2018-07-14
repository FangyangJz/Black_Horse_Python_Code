# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/8

# 之前都是拿 函数 来装饰 函数, 现在是拿 类 来装饰 函数

# class Test(object):
#
#     def __call__(self, *args, **kwargs):
#         print('-------test-------')
#
# t = Test()
# t()  # 因为 __call__ 所以类实例化的对象才能直接()调用
#
##############################################################

class Test(object):

    def __init__(self, func):
        print('初始化')
        print('func name is %s' % func.__name__)
        self.__func = func    # 创建一个[属性],指向func

    def __call__(self, *args, **kwargs):
        print('装饰器中的功能')
        self.__func()    # 这里回去调用类外面的函数

# 定义一个普通的函数
@Test   # 相当于 test = Test(test), 会自动调用 __init__(self), test 指向func
def test():
    print('test 函数')

test()  # 这里会去调用 __call__(self)
