# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/29

# 强烈不推荐用 type 创建类!!!!!!!!!!

class Animal(object):

    def eat(self):
        print('-----eat-----')

# 注意两点
# 第一 : bases 父类必须是元组,所以要有逗号, 父类不用双引号
# 第二 : 字典key为空,赋值一个函数的时候, 报错啊

Cat = type('Cat',(Animal,),{})
xiaomao = Cat()
xiaomao.eat()

# MyClass = MetaClass() # MetaClass 就是用type创建的元类
# MyObject = MyClass()
# Cat.__class__ 可以看到元类
# 用 __metaclass__ = xxxx 可以指定一个类是由哪个元类创建
print(Cat.__class__)

# !!!!!有个 python2 和 python3 的metaclass指定的区别案例!!!