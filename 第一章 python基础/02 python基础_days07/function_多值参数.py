# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/13

# 一个函数 能够处理的参数 个数 是不确定的，这时使用 多值参数
# 1.参数名前增加一个* 可以接收 元祖 ，一般起名为 *args
# 2.参数名前增加两个* 可以接收 字典 ，一般起名为 **kwargs


def demo(num, *nums, **person):

    print num
    print nums
    print person

demo(1)
demo(1, 2, 3, 4, 5, name = "xiaoming", age = 18)