# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5

# a = [x*2 for x in range(10)]
# 当生成的数目非常多的时候,就卡死了,此时就需要生成器
# 生成器,把计算方法保存,用一个生成一个

生成器:
(1) 把列表的[] 换成 ()
    a = (x*2 for x in range(10))
    next(a)     一次就能生成一个

(2) def creatNum():
        a,b = 0,1
        for i in range(5):
            yield b   # 这里!
            a,b = b, a+b


调用方法:
<1>
    x = creatNum()
    next(x)    # 不知道什么时候截至
    a.__next__()  # 和上面一行效果一样

<2>
    for n in a:
        print(n)




