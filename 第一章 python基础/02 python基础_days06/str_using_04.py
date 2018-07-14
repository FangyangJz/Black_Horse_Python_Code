# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/25

from __future__ import print_function


poem = ['登鹳雀楼',
        '王之涣',
        '白日依山尽',
        '黄哥入海流']

# print(str(poem).decode('string_escape'))
# print (poem)

for poem_str in poem:

    print('|%s|' % (poem_str.center(20,' ')))
    print('|%s|'%(poem_str.ljust(20)))
    print('|%s|' % (poem_str.rjust(20)))
