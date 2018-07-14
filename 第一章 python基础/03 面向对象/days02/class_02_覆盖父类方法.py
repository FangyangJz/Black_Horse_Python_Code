# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/20


class Animal:

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

        print ("新的叫法！嗷嗷！")


xtq = XiaoTianQuan()

#如果子类中，重写了父类的方法
#在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()