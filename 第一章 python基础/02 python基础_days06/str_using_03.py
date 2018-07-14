# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/25

hello_str = 'hello world'

# 1. 判断是否以指定字符串开始
print hello_str.startswith("hel")

# 2. 判断是否以指定字符串结束
print hello_str.endswith("ld")

# 3. 查找指定字符串,index同样可以查找字符串中的索引
# index 如果指定的字符串不存在，会报错
# find 如果指定的字符串不存在，会返回-1
print hello_str.find("llo")
print hello_str.find('add')

# 4. 替换字符串
print hello_str.replace('l','TT')
print hello_str