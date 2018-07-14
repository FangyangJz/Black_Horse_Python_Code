# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/13

# 小猫爱吃鱼，小猫爱喝水

class Cat:

    def eatfish(self):
        print "吃鱼"

    def drinkwater(self):
        print "喝水"

xiaomao = Cat()

xiaomao.eatfish()
xiaomao.drinkwater()

print xiaomao

addr = id(xiaomao)
print "%d" % addr
print "%x" % addr