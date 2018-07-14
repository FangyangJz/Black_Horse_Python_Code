# *-* coding:utf-8 *-*
# Author:Fangyang  Time:2017/12/15


import 导入模块调用函数，在修改模块后，执行程序还是导入之前的结果
如果需要将修改导入，方法有二：
1. 重启ipython，重新导入模块
2. from imp import *
    reload(模块)

