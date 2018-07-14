# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/5


# 1. 设计一个Game类
#
# 2. 属性：
#     定义一个 类属性 top_score 记录游戏的历史最高分
#     定义一个 实例属性 player_name 记录当前游戏玩家的姓名
#
# 3. 方法：
#     静态方法 show_help 显示游戏帮助信息
#     类方法 show_top_score 显示历史最高分
#     实例方法 start_game 开始当前玩家的游戏
#
# 4. 主程序步骤：
#     1）查看帮助信息
#     2）查看历史最高分
#     3）创建游戏对象，开始游戏


class Game(object):

    top_score = 0

    def __init__(self,name):

        self.name = name

    @staticmethod
    def show_help():
        print "显示游戏帮助"

    @classmethod
    def show_top_score(cls):
        print "历史最高分：%d " % cls.top_score

    def start_game(self):
        print "%s，游戏开始了" % self.name


Game.show_help()
Game.show_top_score()
xiaoming = Game("小明")
xiaoming.start_game()

# 案例小结
# 1. 实例方法 -- 方法内部需要访问 实例属性
#     实例方法 内部可以使用 类名.访问类属性
# 2. 类方法 -- 方法内部 只 需要访问 类属性
# 3. 静态方法 -- 方法内部，不需要访问 实例属性 和 类属性