# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/9

# 会先搜索当前目录下的模块，如果没有会去搜索系统目录
import random

rand = random.randint(0,10)
print rand

print random.__file__