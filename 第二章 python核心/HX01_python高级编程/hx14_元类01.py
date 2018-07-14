# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/8

# ORM 映射有关
# 在python中一切皆为对象, 类 也是 对象, 占用空间

class Person(object):
    num = 0
    print('--person class--') # 后面不用实例化,这里也执行了,说明类是个对象

    def __init__(self):
        self.name = 'abc'

#####################################
# 动态地创建类(老师不推荐使用)
def choose_class(name):
    ''' 实现了动态创建类的方法'''
    if name == 'foo':
        '''条件满足了, 创建Foo类'''

        class Foo(object):
            pass
        return Foo

    else:
        '''条件不满足, 创建Bar类'''
        class Bar(object):
            pass
        return Bar

MyClass = choose_class('foo')
print(MyClass)
print(MyClass())
print('='*100)
####################################################
# 使用type创建类, type不但可以测试类型, 还可以动态的创建类
# 格式: type(类名, 由父类名称组成的元组(针对继承的情况,可以为空), 包含属性的字典(名称和值))

# type三个参数,
# 第一个参数 : 要创建的类的名字,
# 第二个参数 : 要继承的类, 谁也不继承就(),像下面这种
# 第三个参数 : 字典形式的键值对, 类的属性
Test2 = type('Test2',(),{'num':0})   # type创建类, 这不就是 元类 么, 创建类的哥们
t2 = Test2()
print( type(t2) )
print( type(MyClass()) )
print(t2.num)
print('#'*100)
######################################################
def printNum(self):
    print('num is %d' % self.num)
# 想把以上方法 加入到type创建的类中去
Test3 = type('Test3',(),{'printNum':printNum})
t3 = Test3()
t3.num = 100
print(t3.printNum())