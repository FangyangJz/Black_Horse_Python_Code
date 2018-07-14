# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/7

class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coord: " + str(self.__dict__)

one = Coordinate(100, 200)
two = Coordinate(300, 400)

print(one.__dict__)
print(one)
print(one.x)

