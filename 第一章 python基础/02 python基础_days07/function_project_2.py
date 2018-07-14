# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/13


def demo(num, num_list):

    print "函数开始"

    num += num

    # num_list = num_list + num_list 【这种表达方式不会改变gl变量】

    num_list += num_list
    # 列表+=本质上在调用列表的 extend 方法 【这两种会改变 gl 变量】
    num_list.extend(num_list)

    print num
    print num_list

    print "函数完成"

gl_num = 9
gl_num_list = [1,2,3]
demo(gl_num, gl_num_list)
print gl_num
print gl_num_list
