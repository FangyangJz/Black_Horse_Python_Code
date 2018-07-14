# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/9

# 每一个被开发出来的py文件都应该是可以被导入的
# 全局变量、函数、类应该是模块中可以被调用的量
# 直接执行，如print 不是向外界提供的工具

# __name__属性可以做到，测试模块的代码 只在测试情况下被运行，而在 被导入时不被执行

def say_hello():
    print ("你好好你好！")

# 如果直接执行，都是__main__
# 下面这些为模块内的 测试部分，在其他模块调用时，不会被执行
if __name__ == "__main__":
    print __name__
    say_hello()
