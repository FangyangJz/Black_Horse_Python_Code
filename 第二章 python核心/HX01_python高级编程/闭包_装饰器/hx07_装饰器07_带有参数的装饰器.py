# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5

# 在没有修改函数的情况下,对函数的功能进行了扩展

def func_arg(arg):

    def func(functionName):

        def func_in(*args, **kwargs):
            print('记录日志---arg是:%s' % arg)
            if arg == 'heihei':  # 装饰器带参数在这里可以加判断
                functionName()
                functionName()
            else:
                functionName()

        return func_in

    return func
# 1. 先执行func_arg('heihei')函数,这个函数return的结果是func这个函数的引用
# 2. @func
# 3. 使用@func对test进行装饰

@func_arg('heihei')   # 这里带参数
def test():
    print('---test---')


@func_arg('hahahehee')
def test2():
    print('---test2---')

test()
test2()