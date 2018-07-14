# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/9

# package 的命名规则 ： 小写字母 + _

# 要在外界使用 包 中的模块，需要在 __init__.py 中指定对外界提供的模块列表

from . import send_message
from . import receive_message