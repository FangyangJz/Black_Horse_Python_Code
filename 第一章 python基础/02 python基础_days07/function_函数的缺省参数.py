# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/13

# 函数缺省的参数一般设置为默认最常用的值

gl_list = [6,3,9]

gl_list.sort()
# 默认是升序排序

print gl_list

gl_list.sort(reverse=True)
# 如果需要降序排序，需要指定reverse参数

print gl_list