# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/7

try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 使用8除以用户输入的整数并且输出
    result = 8/num
    print(result)

except ZeroDivisionError:
    print ("除0错误")

except NameError:
    print ("NameError")

except ValueError:
    print ("ValueError")

# 如果输入字母，python3 会抛出ValueError ， python2是 NameError
