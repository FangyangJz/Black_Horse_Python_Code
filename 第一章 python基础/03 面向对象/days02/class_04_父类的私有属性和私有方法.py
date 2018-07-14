# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/3

# 1.子类对象 不能在自己的方法内部，直接访问父类的 私有属性 和 私有方法
# 2.子类对象 可以通过父类的 公有方法 间接访问到 私有属性 或 私有方法

class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):

        print "私有方法 %d %d" % (self.num1,self.__num2)

    def test(self):

        print("父类的公有方法，调用父类中的私有属性%d" % self.__num2)

        self.__test()


class B(A):

    def demo(self):

        # 1. 在子类的对象方法中，不能访问父类的私有属性
        # print ("访问父类的私有属性 %d" % self.__num2)

        # 2. 在子类的对象方法中，不能调用父类的私有方法
        # self.__test()

        # 3. 访问父类的公有属性
        print ("子类方法中调用父类公有属性 %d" % self.num1)


        # 4. 调用父类的公有方法
        self.test()
        pass


b = B()
print b

print b.num1
b.test()

# 在外界不能直接访问对象的私有属性/调用私有方法
# print b.__num2
# print b.__test

#在主程序中，让子类对象调用父类中的公有属性和公有方法
b.demo()