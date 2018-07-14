# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/23

# 1.判断空白字符
space_str = ' \t\n\r'
print space_str.isspace()

space_str = ' a'
print space_str.isspace()
print '-----------------------------------------------'
# 2.判断字符串中是否只包含数字
num_str = '1'
print num_str.isalnum()
print num_str.isdigit()  #都不能判断小数
# print num_str.isdecimal()  python3
# print num_str.isnumeric()