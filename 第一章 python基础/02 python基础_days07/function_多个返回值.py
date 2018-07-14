# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/12


def measure():
    """测量温度和湿度"""

    print ("测量开始。。。")
    temp = 39
    wetness = 50
    print ("end。。。")

    # tuple 可以包含多个数据，因此可以使用tuple让函数一次返回多个值
    return temp, wetness  # 函数返回的是元组，即便没有加 ()


result = measure()
print result

#需求：需要单独的处理温度或湿度
print result[0]
print result[1]

# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数应该和元祖中的元素数量保持一致
gl_temp, gl_wetness = measure()
print gl_temp
print gl_wetness