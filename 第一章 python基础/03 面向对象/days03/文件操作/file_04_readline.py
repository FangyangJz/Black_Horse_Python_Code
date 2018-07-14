# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/10

# read方法默认会把文件的所有内容一次性读取到内存
# 如果文件太大，对内存的占用会非常严重

file = open("readme.txt")


while True:

    text = file.readline()

    # 判断是否读取到内容，如果没有，break
    # if text == '':
    #     break
    if not text:
        break

    print text


file.close()