# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/12

# 1. 有两个整数变量 a = 6 ，b = 10
# 2. 不使用其他变量，交换两个变量的值

a = 6
b = 10

# 解法1
# c = a
# a = b
# b = c

# 解法2
# a = a + b
# b = a - b
# a = a - b

# 解法3  - python专有
a, b = (b, a)  # 小括号可以省略

print a
print b