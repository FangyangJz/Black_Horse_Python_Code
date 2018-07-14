# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/28

# & 按位与
# | 按位或
# ^ 按位异或
# ~ 按位取反
# << 按位左移 比乘法效率高
# >> 按位右移

# 0b0010 == 2
# 0o0010 == 8
# 0x0010 == 16
# 函数 bin(),oct(),hex()

print(5<<1)
a = 0b0011
print(hex(100),type(hex(100)))
print(~0x0010)