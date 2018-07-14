# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/22

xiaoming = {'name':'xiaoming',
            'age':18,
            'gender':True,
            'height':1.75}

print(xiaoming.keys())
print(xiaoming.values())
print(xiaoming.items())
print(xiaoming)

# 1取值
print(xiaoming['height'])

# 2增加/修改
xiaoming['age'] = 20
xiaoming['体重'] = 98

print(xiaoming)

# 3删除
xiaoming.pop("name")
print(xiaoming)