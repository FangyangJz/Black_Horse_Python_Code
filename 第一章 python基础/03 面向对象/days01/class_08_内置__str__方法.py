# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/19

#在开发时想用print输出一些自定义的内容，就要用__str__方法，必须反回一个字符串

class Cat:

    def __init__(self,newname):

        self.name = newname

        print ("%s 来了" % self.name)

    def __del__(self):

        print("%s 我去了" % self.name)

    def __str__(self):

        #必须返回一个字符串
        return "我是小猫【%s】"%self.name

# tom是一个全局变量
tom = Cat("Tom")
print(tom)