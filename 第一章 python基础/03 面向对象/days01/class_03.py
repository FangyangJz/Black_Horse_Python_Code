# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/14


class Cat:

    def eatfish(self):
        print "吃鱼"

    def drinkwater(self):
        print "喝水"

xiaomao = Cat()

# 可以使用  .属性名  利用赋值语句就可以了
# 在类的外面给对象设置属性，非常容易，但是不推荐
xiaomao.name = "Tom"

xiaomao.eatfish()
xiaomao.drinkwater()

print xiaomao


#再创建一个猫对象
lazy_cat = Cat()
lazy_cat2 = lazy_cat

lazy_cat.drinkwater()
lazy_cat.eatfish()

print lazy_cat
print lazy_cat2