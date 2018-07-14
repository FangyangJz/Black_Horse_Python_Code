# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/29

# 1. 小整数对象池 [-5, 257) 这个范围是提前建立好的
# 我去! 貌似 python3 不是这么回事啊
# python2 貌似也不是这么回事啊
a = 100
b = 100
c = 100
print(id(a), id(b), id(c))

# 2. 大整数池机制, 貌似也不是那么回事啊
A = 1000
B = 1000
print(id(A), id(B))

# 3. intern机制
# 对于不可变类型, 比如字符串, 都共用一份内存
# 老师说带空格就不一样了, 结果测试下来还是一样的
a1 = 'hello world'
a2 = 'hello world'
a3 = 'hello world'
print(id(a1),id(a2),id(a3))