# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/22

info_tuple = ('zhangsan', 18, 1.75,18,18)
'''tuple中通常保存不同类型的数据，而list中通常保存相同类型的数据'''

single_tuple = (5,)
print type(single_tuple)

# 取值与取索引
print info_tuple[0]
print info_tuple.index(18)

# 统计计数
print info_tuple.count(18)

# 使用迭代遍历元组
for my_info in info_tuple:

    print my_info