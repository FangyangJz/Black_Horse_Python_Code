# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/5


# 类属性 就是给 类对象 中定义的属性
# 通常用来记录 与这个类相关 的特征
# 类属性 不会用于记录 具体对象的特征


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
print Tool.count