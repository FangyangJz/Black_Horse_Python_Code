# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/2


from threading import Thread
import time

# 多线程之间相互独立, 不会相互影响
def test():
    print(t1.name)
    for i in range(3):
        print('---%d---'%i)
        time.sleep(1)


for i in range(5):
    t1 = Thread(target=test)
    t1.start()