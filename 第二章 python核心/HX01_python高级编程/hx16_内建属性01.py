# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/30


class Itcast(object):

    def __init__(self, subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    # 属性访问时拦截器, 可以用于打
    def __getattribute__(self, item):
        if item == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            return object.__getattribute__(self, itelogm)

    def show(self):
        print('This is Itcast')


s = Itcast('python')
print(s.subject1)
print(s.subject2)