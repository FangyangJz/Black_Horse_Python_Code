# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/7


# 在开发时，要预判到所有可能出现的错误，是有一定难度的
# 如果希望程序 无论出现任何错误，都不会因为 python 解释器 抛出异常而被终止，
# 可以再增加一个except Exception as xxxxxx:

try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 使用8除以用户输入的整数并且输出
    result = 8/num
    print(result)

except NameError:
    print ("NameError")

except ValueError:
    print ("ValueError")
#==================================================
except Exception as result:
    print ("未知错误 %s"%result)