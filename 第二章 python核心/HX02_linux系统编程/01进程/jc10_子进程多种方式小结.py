# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/31

# (1) fork, 只用于linux (不推荐)
ret = os.fork()
if ret == 0:
    # 子进程
else:
    # 父进程

# (2) Process(target=xxx), 还有一个 class Xxx(Process):
p1 = Process(target=func)
p1.start()
# 主进程也能干点活

# (3) pool  (推荐)
pool = Pool(3)
pool.apply_async(xxxx)
# 主进程一般用来等待, 不干活, 真正的任务在子进程中执行