# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/3

# 面向对象三大特性：
#     1. 封装 ，根据职责将 属性和方法 封装 到一个抽象的 类 中
#     2. 继承 ，实现代码的重用，相同的代码不需要重复编写
#     3. 多态 ，不同的 子类对象 调用相同的父类方法，产生不同的执行结果


class Dog(object):

    def __init__(self,name):

        self.name = name

    def game(self):

        print "%s 蹦蹦跳跳的玩耍" % self.name


class XiaoTianQuan(Dog):

    def game(self):

        print "%s 飞到天上去玩耍" % self.name


class Person(object):

    def __init__(self,name):

        self.name = name

    def game_with_dog(self,dog):

        print "%s 和 %s 快乐的玩耍" % (self.name,dog.name)

        # 让狗玩耍
        dog.game()

# 1 创建一个狗对象

# wangcai = Dog("旺财")
wangcai = XiaoTianQuan("飞天旺财")

# 2 创建一个小明对象
xiaoming = Person("小明")

# 3 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)