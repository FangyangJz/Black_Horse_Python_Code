# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/10


# open函数默认以 只读 方式打开文件，并且返回文件对象
# r 只读方式打开
# w 只写方式打开，如果文件存在覆盖，不存在创建
# a 追加方式打开文件，文件存在，文件指针指向末尾，如果文件不存在，创建新文件写入

# 下面这三种比较少用
# r+ 以读写方式打开文件，与r区别：文件不存在，会抛出异常
# w+ 以读写方式打开文件，如果文件存在就覆盖，文件不存在创建
# a+ 以读写方式打开文件，同a


file = open("readme.txt",'a')

file.write("write heell")

file.close()