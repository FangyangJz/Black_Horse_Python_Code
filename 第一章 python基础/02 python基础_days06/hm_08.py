# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/21

def print_line(char,times):
    '''打印分隔符（符号，次数）'''

    print(char*times)

def print_lines(char,times):
    '''打印多行分割线

    :param char: 分割线使用的字符
    :param times: 重复次数
    '''

    row = 0

    while row < 5:
        print_line(char,times)
        row += 1

print_lines('&',10)

name = 'heima chengxuyuan'