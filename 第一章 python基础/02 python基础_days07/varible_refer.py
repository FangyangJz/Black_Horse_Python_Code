# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/12


def test(num):

    print ("在函数内部 %d 对应的内存地址是 %d" % (num,id(num)))

    # 1.定义一个字符串变量
    result = "hello"
    print ("函数要返回数据的内存地址是 %d" % id(result))

    # 2.将字符串变量返回,返回的是数据的引用，而不是数据本身
    return result

# 1.定义一个数字的变量


a = 10

print ("a变量保存数据的内存地址是 %d" % (id(a)))

# 2.调用test函数,本质上传递的是实参保存数据的引用，而不是实参保存的数据
r = test(a)
print ("%s 的内存地址是 %d" % (r, id(r)))
