# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/28


class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value,int):
            self.__money = value
        else:
            print('error:不是整型数字')

    money = property(getMoney, setMoney) # 注意这里不要写()

t = Money()
t.money = 200  # 相当于调用了 t.setMoney(200)
print(t.money) # 相当于调用了 t.getMoney()

# property 相当于用 属性的方式 掩盖 调用函数 这种复杂的调用方式

