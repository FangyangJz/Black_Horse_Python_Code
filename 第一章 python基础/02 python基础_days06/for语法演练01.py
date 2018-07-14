# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/3

import os

for num in [1,2,3]:

    print(num)

    if num == 2 :
        break
else:
    # 如果for循环中的break被执行了，else中的代码就不会被执行
    print("is it exe?")

print("the end")

os.fork()
