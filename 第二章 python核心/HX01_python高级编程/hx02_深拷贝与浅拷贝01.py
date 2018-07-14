# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/28

a = [11,22,33]
b = a
print(id(a))
print(id(b)) # id 相同，浅拷贝

print('-'*50)

import copy
c = a.copy()
d = copy.deepcopy(a)
print(id(c)) # id 不同深拷贝
print(id(d))

print('='*50)

a = [11,22,33]
b = [44,55,66]
c = [a,b]
d = c
e = copy.deepcopy(c)
a.append(44)
print(c)
print(e) # 把列表里面的引用指向的内容都拷贝了，太深了

print('|'*100)
a = [11,22,33]
b = [44,55,66]
c = [a,b]
d = copy.copy(c)   # 区分deepcopy 和 copy
a.append(99)
print(c[0])
print(d[0])