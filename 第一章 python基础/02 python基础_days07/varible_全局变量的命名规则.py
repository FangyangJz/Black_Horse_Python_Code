# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/12


gl_num = 10
# 全局变量要加 g_ 或者 gl_ 前缀
# 可以右键refactor，一起修改全模块中出现的局变量

def demo1():

    num = 99
    # 如果局部变量的面子和全局变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的虚线
    print ("demo1 ==> %d" % num)


def demo2():

    print ("demo2 ==> %d" % gl_num)


demo1()
demo2()