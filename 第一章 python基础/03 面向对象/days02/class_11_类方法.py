# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/5

    # 定义类方法格式 ：
  #  @classmethod
  #  def 类方法名(cls):
  #     pass


class Tool(object):

    # 使用赋值语句定义 类属性，记录所有工具对象的数量
    count = 0

    #定义类方法
    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)


    def __init__(self,name):

        self.name = name
        # 每次调用初始化方法的时候，让类属性的值加1
        Tool.count += 1

tool1 = Tool("Axe")
tool2 = Tool("hammer")

Tool.show_tool_count()