# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/13


def demo(*args, **kwargs):

    print args
    print kwargs


gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

demo(*gl_nums, **gl_dict)
#ctrl+p 查看参数信息 ，在参数前加*号，叫拆包

demo(1, 2, 3, name="小米", age=18)
# 不用*号，就要自己手动拆包，像这样，dict的key不要加“”，要用=
