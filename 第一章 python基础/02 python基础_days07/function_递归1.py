# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/13


def sum_numbers(num):

    if num == 1 :
        return 1 #这里如果 return None ，相当于下一次temp为 None 和 int做加和

    temp = sum_numbers(num-1)

    return (temp + num)


print (sum_numbers(100))