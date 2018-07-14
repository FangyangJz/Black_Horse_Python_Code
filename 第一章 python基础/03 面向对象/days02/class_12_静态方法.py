# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/5


# 在开发时，如果需要在 类 中封装一个方法，这个方法：
# 既 不需要 访问 实例属性 或者调用 实例方法
# 也 不需要 访问 类属性 或者调用 类方法
# 这个时候，可以把这个方法封装成一个静态方法

#语法如下 :
# @staticmethod
# def 静态方法名():
#     pass

class Dog(object):

    @staticmethod
    def run():
        print "小狗要跑。。。"

# 通过类名.调用静态方法。 不需要创建对象 就可以调用
Dog.run()