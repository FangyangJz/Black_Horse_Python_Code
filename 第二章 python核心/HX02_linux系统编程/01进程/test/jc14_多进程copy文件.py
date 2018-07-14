# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/1


import os

# 0. 获取要copy文件夹的名字
old_folder_name = input('请输入要拷贝的文件夹名字:')
# new_folder_name = old_folder_name + '-复件'

# 1. 创建一个文件夹
# print(new_folder_name)
# os.mkdir(new_folder_name)

# 2. 获取old文件夹中的所有文件的名字
lst = os.listdir(old_folder_name)
print(lst)
# 3. 使用多进程方式copy原文件夹中的文件到新文件夹中