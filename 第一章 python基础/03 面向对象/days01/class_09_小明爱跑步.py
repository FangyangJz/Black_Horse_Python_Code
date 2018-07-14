# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/19


class Person:

    def __init__(self, newname, weight):

        # self.属性 = 形参
        self.name = newname
        self.weight = weight

    def __str__(self):

        return "我的名字叫 %s , 体重 %0.1f kg" % (self.name, self.weight)

    def run(self):

        print "%s 爱跑步，跑步锻炼身体" % self.name
        self.weight = self.weight - 1

    def eat(self):

        print "%s 爱吃，吃增加体重" % self.name
        self.weight = self.weight + 2


xiaoming = Person("小明", 75.0)
xiaoming.eat()

xiaomei = Person("小美", 48.0)
xiaomei.run()

print xiaoming
print xiaomei
