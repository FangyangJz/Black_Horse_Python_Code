# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/10


file_read = open("readme.txt")
file_write = open("readme[copy].txt",'w')

text = file_read.read()
file_write.write(text)


file_read.close()
file_write.close()
