# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/3


# 不同父类中存在同名的方法，子类对象在调用方法时，会调用混淆

class A:

    def test(self):

        print "A----test 方法"

    def demo(self):

        print "A----demo 方法"


class B:

    def test(self):

        print "B----test 方法"

    def demo(self):

        print "B----demo 方法"


class C(A,B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


c = C()
c.test()
c.demo()

# 确定C类对象调用方法的顺序. python2 中貌似没有mro
# print (C.__mro__)