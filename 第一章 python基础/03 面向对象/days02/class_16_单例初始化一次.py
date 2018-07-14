# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/7


class MusicPlayer(object):

    instance = None

    #记录是否执行过初始化方法
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否是None
        # 2.调用父类的方法，为第一个对象分配空间
        # 3.返回类属性保存的对象引用

        if cls.instance is None:

            cls.instance = super().__new__(cls)


        return cls.instance

    def __init__(self):

        #1.判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        #2.如果没有执行过，执行初始化动作

        #3.修改类属性标记
        print ("初始化播放器")
        MusicPlayer.init_flag = True

# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
