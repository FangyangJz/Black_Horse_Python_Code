# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/25

poem_str = '登鹳雀楼\t 王之涣 \t 白日衣衫尽  \t \n 黄河入海流  \t\t'

print poem_str
# 1.将字符串中的空白字符全部去掉
# 2.再次使用 " " 作为分隔符，拼接成一个整齐的字符串

# 1.拆分字符串
poem_list = poem_str.split()
print str(poem_list).decode(encoding='string_escape')

# 2.合并字符串

