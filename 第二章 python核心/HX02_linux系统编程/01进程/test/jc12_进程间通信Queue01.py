# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/31


from multiprocessing import Queue

q = Queue(3)  # 如果这里啥都不写, Queue无限大jc12_进程间通信Queue.py
print(q.qsize())
q.put('haha-1')
print(q.qsize())
q.put('haha-2')
print(q.qsize())
q.put('haha-3')
print(q.qsize())
# q.put('haha-4')  # 当队列加满的时候, 再put就要等前面有空位了,程序就卡在这了
# print(q.qsize())
print(q.get())  # 当队列中的内容全都取完后, 再get(), 就堵塞等着了
print(q.qsize())
# q.empty(), 判断队列是否为空, get前一般用中这个判断下
# q.full(), 判断队列是否满, put前一般用这个判断下
# q.get_nowait() , 堵塞了也不等, 会返回异常, 一般放在try里
# q.put_nowait() , 同上