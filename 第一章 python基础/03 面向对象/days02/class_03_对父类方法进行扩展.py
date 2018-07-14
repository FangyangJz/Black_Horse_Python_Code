# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/21


# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/20


class Animal(object):

    def __init__(self):

        pass

    def eat(self):

        print "吃"

    def drink(self):

        print "喝"


class Dog(Animal):

    def bark(self):

        print "旺！旺！"


class XiaoTianQuan(Dog):

    def fly(self):

        print "I can fly"

    def bark(self):

        # 1. 针对子类特有的需求，编写代码
        print "哮天犬独有吼叫！"

        # 2. 使用super()，调用原本在父类中封装的方法

# 在python3中，super().bark() 直接调用上级父类的方法
# 在python2中，super要写成下面这种格式，同时 根基父类 要继承 object，否则要报错

        # super(XiaoTianQuan, self).__init__()
        super(XiaoTianQuan, self).bark()

# 在python2中，还可以用下面这种方法调用父类中的方法 父类名.方法(self) 【不推荐使用】
        Dog.bark(self)

        # 3. 增加其他子类的代码
        print "!@#$%^&*"*3



xtq = XiaoTianQuan()

xtq.bark()