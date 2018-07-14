# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/31


from multiprocessing import Process
import time

# 这个程序主进程在跑完后并没有结束, 而是等子进程结束
# 这点和 fork 不一样
def test():
    for i in range(5):
        print('---test---')
        time.sleep(1)

if __name__ == '__main__':

    p = Process(target=test)
    p.start() # 让这个进程执行test函数中的代码
    p.join()  # 堵塞. 主进程在这里等着子进程
    # p.terminate() # 直接结束子进程
    print('----main----')
