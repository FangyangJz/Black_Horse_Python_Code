# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/2


import threading
import time

class MyThread(threading.Thread):

    def run(self):
        '''在多线程对象实例化后, .start开始必启动run方法'''
        # 在run方法中重写, 写你希望实现的功能
        for i in range(3):
            time.sleep(1)
            msg = "I'm" + self.name + '@' +str(i)
            print(msg)

if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()
    t3 = MyThread()
    t1.start()
    t2.start()
    t3.start()