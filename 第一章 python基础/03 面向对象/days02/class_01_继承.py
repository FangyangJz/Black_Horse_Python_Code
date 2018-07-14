# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/19


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

wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.bark()
print "-"*50

xtq = XiaoTianQuan()
xtq.fly()
xtq.eat()
xtq.bark()