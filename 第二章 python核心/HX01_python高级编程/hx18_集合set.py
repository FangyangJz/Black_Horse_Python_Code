# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/30


a = [1,2,3,4,5,6]
b = [4,5,6,7,8,8,8,8,8]
a = set(a)
b = set(b)
# 集合中的逻辑运算
print(a&b)
print(a|b)
print(a-b) # 差集
print(a^b) # 对称差集