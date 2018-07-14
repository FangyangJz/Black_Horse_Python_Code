# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/19


class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def secret(self):

        print ("%s 的年龄是 %d" % (self.name, self.__age))

    def __secret(self):

        print ("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")
# print xiaofang.__age 【私有属性】  在外部不能够被直接访问
# 在 对象非私有方法中的私有属性是可以访问的
xiaofang.secret()

print "-"*50

# xiaofang.__secret() 【私有方法】  是无法在外部访问的
# 如果想访问【不推荐】，参考以下方法
print xiaofang._Women__age
xiaofang._Women__secret()