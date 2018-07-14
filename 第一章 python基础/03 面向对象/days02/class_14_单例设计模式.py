# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/5


class MusicPlayer(object):

    # 重写 __new__ 方法
    def __new__(cls, *args, **kwargs):
        # *args 代表多值的元组参数 ， **kwargs 代表多值的字典参数
        # 1. 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")
        # 重写__new__方法一定要 return super().__new__(cls)
        # 否则python的解释器得不到分配了空间的对象引用，就不会调用对象的初始化方法
        # 注意：__new__是一个静态方法，在调用时需要主动传递 cls 参数

        # python3 写法：
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()
print(player)
