# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/18


class Cat:

    def __init__(self,newname):

        self.name = newname

        print ("%s 来了" % self.name)

    def __del__(self):

        print("%s 我去了" % self.name)

# tom是一个全局变量
tom = Cat("Tom")
print tom.name

# 在我们删除tom时，系统会调用__del__方法，所以在横线上方输出。
del tom
# 没有del操作的时候，在执行完整个程序后，系统会调用__del__方法，所以在横线下输出

print "-"*50