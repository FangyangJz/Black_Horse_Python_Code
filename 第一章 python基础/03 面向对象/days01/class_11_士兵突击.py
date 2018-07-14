# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/19


# 一个对象的 属性 可以是另一个类创建的对象

# 需求
# 1.士兵 许三多 有一把 AK47
# 2.士兵 可以开火
# 3.枪 能够 发射子弹
# 4.枪 装填子弹 -- 增加子弹数量


class Gun:

    def __init__(self, model):

        # 从外部来的枪的名字
        self.model = model

        # 内部初始设置为0颗子弹
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count = self.bullet_count + count

    def shoot(self):

        # 1 判断子弹数量
        if self.bullet_count > 0:

            self.bullet_count = self.bullet_count - 1

            print "[%s] biu ! ~~~子弹剩余[%d]" % (self.model, self.bullet_count)

        else:

            print "%s 里没子弹了。。。" % self.model

            return


class Soldier:

    def __init__(self, name):

        self.name = name

    # 定义属性时，如果不知道设置什么初始值，可以设置为 None
    # 因为新兵没有枪，不知道什么枪

        self.gun = None

    def fire(self):

        # 1 判断士兵是否有枪
        if self.gun is None:

            # a = [1, 2, 3]
            # id(a)
            # Out[3]: 56308360
            # b = [1, 2]
            # id(b)
            # Out[5]: 56346504
            # b.append(3)
            # id(b)
            # Out[7]: 56346504
            # a == b
            # Out[8]: True
            # a is b
            # Out[9]: False

            print "[%s] 没有枪" % self.name
            return

        # 2 高喊口号

        print ("冲啊。。。【%s】" % self.name)

        # 3 让枪装填子弹

        self.gun.add_bullet(50)

        # 4 让枪发射子弹

        self.gun.shoot()


ak47 = Gun("AK47")
# ak47.add_bullet(10)
# ak47.shoot()

xsd = Soldier("许三多")
xsd.gun = ak47
xsd.fire()
