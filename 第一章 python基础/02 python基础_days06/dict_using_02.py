# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/22

xiaoming = {'name':'xiaoming',
            'age':18,
            'gender':True,
            'height':1.75}

# 1 统计 键值对 数量
print len(xiaoming)

# 2 合并字典
temp_dict = {'weight':90,
             'name':'M'}
xiaoming.update(temp_dict)
# 如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
print xiaoming

# 3 清空字典
xiaoming.clear()
print xiaoming