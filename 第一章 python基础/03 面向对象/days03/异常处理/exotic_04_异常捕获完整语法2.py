# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/7


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

else:
    print ("尝试成功，没有异常")

finally:
    print ("无论是否出现异常，都会被执行")