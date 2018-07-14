# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/30


class Itcast(object):

    def __init__(self, subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    # 属性访问时拦截器, 可以用于打
    def __getattribute__(self, item):

        print('=======1>%s'%item)

        if item == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            temp = object.__getattribute__(self, item)
            print('=========2>%s'%str(temp))
            # 注意下面这句, 千万注意不能写成 self.__getattribute__, 那样死循环
            return object.__getattribute__(self, item)

    def show(self):
        print('This is Itcast')


s = Itcast('python')
print(s.subject1)
print(s.subject2)
s.show()
# 1. 先获取show属性对应的结果, 应该时一个方法
# 2. 方法()