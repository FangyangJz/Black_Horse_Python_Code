# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/9


import package

package.send_message.send("hello")
txt = package.receive_message.receive()
print txt