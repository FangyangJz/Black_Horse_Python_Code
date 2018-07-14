# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/9

# 如果导入的模块中存在同名函数，那么调用时，后面导入的函数会覆盖前面的
# 可以用 import 。。。 as 。。。 规避上面的问题

from module_01 import *   # 全部导入，但是say_hello函数被后面覆盖了
from module_01 import Cat
from module_02 import say_hello
from module_02 import Dog as DD

say_hello()

miaomiao = Cat()
print (miaomiao)

wangcai = DD()
print (wangcai)