# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5



# 判断是否是 可迭代的
from collections import Iterable
a = isinstance([], Iterable)
print(a)

# 迭代器: 可以用 next() 的都叫迭代器,所以生成器都是迭代器
# 判断是否是 迭代器
from collections import Iterator
isinstance((x for x in range(10)), Iterator)
# 上面返回 True
isinstance([], Iterator)
# 上面返回 False

# 生成器一定是迭代器, 但是迭代器不一定都是生成器
# iter()函数, 可以把list, tuple, str等 Iterable 转变成 Iterator
a = [1,2,3,4,5]
b = iter(a)
next(b)