# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/9


# 在计算机中要操作文件的套路非常固定，一共包含三个步骤：
# 1. 打开文件     open
# 2. 读写文件
#     读，将文件内容读入内存     read
#     写，将内存内容写入文件     write
# 3. 关闭文件     close


# 为了防止系统资源的消耗，程序员会在打开文件后马上写关闭文件，测试没问题了再在中间写代码
file = open("readme.txt")

text = file.read()
print text

file.close()