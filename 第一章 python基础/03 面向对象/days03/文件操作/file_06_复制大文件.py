# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/10


file_read = open("readme.txt")
file_write = open("readme[copy].txt",'w')


while True:

    text = file_read.readline()

    if not text:
        break

    file_write.write(text)


file_read.close()
file_write.close()