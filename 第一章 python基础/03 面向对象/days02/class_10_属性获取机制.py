# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/5

# 在python中，属性的获取存在一个向上查找的机制

class Tool(object):

    # 使用赋值语句定义 类属性，记录所有工具对象的数量
    count = 0

    def __init__(self,name):

        self.name = name
        # 每次调用初始化方法的时候，让类属性的值加1
        Tool.count += 1


# 1 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 2 输出工具对象的总数
# print Tool.count
print "工具对象总数 %d" % tool1.count
print tool1.name

# 要访问类属性有两种方法 ：
# 1 类名.类属性
# 2 对象.类属性（不推荐）

# 修改 对象.类属性 的值，会在对象中创建这个属性，而不去修改 类 中 类属性
tool3.count = 99
print tool3.count
print Tool.count