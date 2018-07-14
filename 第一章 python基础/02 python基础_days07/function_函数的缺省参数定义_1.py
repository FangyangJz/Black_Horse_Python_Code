# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/13


def print_info(name, gender = True): # 要缺省gender ，就在参数这里 gender = True
    """

    :param name: 班上同学的姓名
    :param gender: True 男生， False 女生
    """

    gender_text = "男生"

    if not gender:

        gender_text = "女生"

    print ("%s 是 %s" % (name, gender_text))

print_info("xiaoming", True)
print_info("wang")
print_info("xiaomei", False)
print_info("liubing", gender=False)
