# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/10

input_str = raw_input("请输入算术题：")
print type(input_str)
print (eval(input_str))

# 不要滥用eval
# __import__('os').system('ls')
# 等价于
# import os
# os.system('ls')

# 执行成功返回 0
# 执行失败返回错误信息