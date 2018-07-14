# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/28


# xx:公有变量
# _x：单前置下划线，私有化属性或方法，from somemoudule import * 禁止导入，类对象和子类可以访问
# __xx:双前置下划线，避免与子类中的属性命名冲突，无法在外部直接访问（名字重复所以访问不到）,想访问，_类名__xx(系统不推荐)
# __xx__:双前后下划线，用户名字空间的系统方法或属性
# xx_：单后置下划线，用于避免与python关键词冲突 if_ = 100


class Test(object):
    def __init__(self):
        self.num = 100
        self.__num = 1000

    def setNum(self,newNum):
        self.__num = newNum

    def getNum(self):
        return self.__num

t = Test()
t.num = 200
# print(t.__num)  # 这里带__的属性，不能在类外面使用，报错啊
t.__num = 2000
print(t.num)
print(t.__num)  # 这里可以使用，是因为前面赋值了，相当于添加了一个同名的__num属性

print('-'*50)

print(t.getNum())
t.setNum(50)
print(t.getNum())

