# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/18


class Cat:

    def __init__(self,newname):

        print "这是一个初始化方法"

        #self.属性名 = 属性的初始值
        #self.name = "Tom"
        self.name = newname

    def eatfish(self):

        print ("%s 吃鱼" % self.name)


#使用类名（）创建对象的时候，会自动调用初始化方法 __init__
tom = Cat("Tom")
tom.eatfish()

lazy_cat = Cat("大懒猫")
lazy_cat.eatfish()