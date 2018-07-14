# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/7

try:
    # 尝试执行的代码
    pass

except 错误类型1:
    # 针对错误类型1，对应的代码处理
    pass

except (错误类型2, 错误类型3):
    # 针对错误类型2和3，对应的代码处理
    pass

except Exception as result:
    # 打印未知错误信息
    print (result)

else:
    # 没有异常才会执行的代码
    pass

finally:
    # 无论是否异常，都会执行的代码
    print ("无论是否有异常，都会执行的代码")