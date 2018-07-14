# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/14


class Cat():

    def eatfish(self):
        print "%s 吃鱼" % self.name

    def drinkwater(self):
        print "%s 喝水" % self.name

xiaomao = Cat()

# 可以使用  .属性名  利用赋值语句就可以了
# 在类的外面给对象设置属性，非常容易，但是不推荐
# 为啥不推荐？要是把下面这行放在后面两个方法的调用，就报错了
xiaomao.name = "Tom"

xiaomao.eatfish()
xiaomao.drinkwater()
