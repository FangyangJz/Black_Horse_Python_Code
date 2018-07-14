# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/10


file = open("readme.txt")

text = file.read()
print (text)
print (len(text))

print "-"*50

text = file.read()
print (text)
print (len(text))

file.close()