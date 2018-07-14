# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/28

import copy

a = [1,2,3]
b = [4,5,6]
c = (a,b)       # tuple 是不可变类型，copy 不创建新 的标签和内容
e = copy.copy(c)
print(id(c))
print(id(e))