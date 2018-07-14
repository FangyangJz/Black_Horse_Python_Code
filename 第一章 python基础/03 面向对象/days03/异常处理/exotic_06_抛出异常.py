# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/7


# python 中提供了一个Exception异常类
# 在开发时，如果满足 特定业务需求时，希望抛出异常，可以：
#     1.创建一个 Exception 的对象
#     2.使用 raise 关键字抛出异常对象
#
# 需求
#     定义 input_password 函数，提示用户输入密码
#     如果用户输入长度<8，抛出异常
#     如果用户输入长度>=8,返回输入的密码

def input_password():
    #1. 提示用户输入密码
    pwd = raw_input("请输入密码：")

    #2. 判断密码长度 >=8, 返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    #3. 如果<8，主动抛出异常
    print ("主动抛出异常")
    # <1>创建异常对象, 可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # <2>主动抛出异常
    raise ex

# 提示用户输入密码
try:
    print(input_password())

except Exception as result:
    print (result)