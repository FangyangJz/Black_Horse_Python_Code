# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/30

# range
# python2 中直接返回一个列表, python3中是一个迭代值
# python2中为了解决上面的问题,用xrange, 更节省空间

# map
# map(function, sequence[,sequence,...]) -> list
x = map(lambda x:x**x, [1,2,3])
print([i for i in x])

x = map(lambda x,y : x+y, [1,2,3],[4,5,6])
print([i for i in x])

#####################################################

def f1(x, y):
    return (x, y)

l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ['Sun', 'M', 'T', 'W', 'T', 'F', 'S']
l3 = map(f1, l1, l2)
print(list(l3))

######################################################
# filter
print(list(filter(lambda x:x%2, [1,2,3,4])))
print(list(filter(None, 'she'))) # None表示不过滤, 全取

###################################################
# reduce
# 在Python 3里，reduce()函数已经被从全局名字空间里移除了，
# 它现在被放置在fucntools模块里用的话要 先引入
from functools import reduce
# 先1和2, 然后 结果和3, 然后 结果和4
print(reduce(lambda x,y : x+y, [1,2,3,4]))
# 5给x 1给y, 结果6给x 2给y, 结果8给x 3给y, 结果11给x 4给y
print(reduce(lambda x,y : x+y, [1,2,3,4],5))
print(reduce(lambda x,y : x+y, ['aa','bb','cc'],'dd'))

########################################################
# sort sorted()
a = [112,23,43,52,62,34,67,89,21]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a = [112,23,43,52,62,34,67,89,21]
aa1 = sorted(a)
print(aa1)
print('-'*50)

a = [112,23,43,52,62,34,67,89,21]
aa1 = sorted(a,reverse=1)
print(aa1)
# 字母也可以排序