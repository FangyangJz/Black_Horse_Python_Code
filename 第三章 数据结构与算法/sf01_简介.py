# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/2


import time

start_time = time.time()

# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 print('a,b,c: %d, %d, %d' % (a, b, c))
# 运行一共花了 times: 177  秒
# T = 1000*1000*1000*2
# 如果到2000, T = 2000*2000*2000*2
# T =N*N*N*2
# T(n) = n^3 * (2或者10) , T(n)叫做时间复杂度
# g(n) = n^3
# T(n) = k*g(n)
# T(n) = O(g(n))

for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 - a - b
        if a**2+b**2 == c**2:
            print('a,b,c: %d, %d, %d' % (a, b, c))
# 运行一共花了 times: 1 秒
# T(n) = n*n * (1+max(1,0))
#      = n^2 * 2
#      = O(n^2)

end_time = time.time()
print('times: %d' % (end_time-start_time))
print('finish')