# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5


class Person(object):

    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print('正在吃....')


laowang = Person('老王', 100)
print(laowang.name)
print(laowang.age)
laowang.addr = '北京'  #这里动态修改 类实例对象 属性
print(laowang.addr)

Person.num = 20       # 这里动态修改 类 属性
print(laowang.num)    # 类实例对象 里面找不到这个属性,回去 类 属性里面去找

###################################################
#  增加类中  [方法]

def run(self):
    print('正在跑....')

# laowang.run = run
# laowang.run()

# 虽然laowang对象中 run属性已经指向了28行的函数run,但是这句代码不对
# 因为run属性指向的函数是后来添加的,laowang.run()的时候,
# 并没有把laowang当作第一个参数传入

##############################################
# 解决方法[动态方法绑定函数]:
import types
laowang.run = types.MethodType(run, laowang)
# 在laowang中添加了一个属性run 指向 外面的 函数run,
# tyeps.MethodType(run, laowang) 相当于一个self参数
laowang.run()
print('#'*100)

###############################################
# 静态方法 添加
@staticmethod
def test():
    print('-----static method------')

Person.test = test
Person.xx = test
Person.test()
laowang.test()
laowang.xx()

print('#'*100)
################################################
# 类方法 添加
@classmethod
def printNum(cls):
    print('--------class method-----------')


Person.printNum = printNum
Person.printNum()

