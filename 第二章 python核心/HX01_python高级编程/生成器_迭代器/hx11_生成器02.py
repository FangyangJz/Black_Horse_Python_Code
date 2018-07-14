# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5

def test():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1

t = test()

t.__next__()  # 第一次执行到yield,在等号右侧停下, 返回一个值
t.__next__()  # 第二次执行,从yield开始,需要向temp赋值,但是上一次的值已经返回了,
              # 此时没有值,
              # 没有返回值,
              # 出一个None, 同时循环一次返回yield下一次的值

# send 和 next 都可以让生成器往下执行一次
# 不同在于, send(value) 相当于把value整体给yield整体
t.send('haha') # 这里就有值了,不会返回None
               # 不能一上来就用 send, 要等一次next后用
               # 上面的替代方法是 第一次send(None)先,然后send()





