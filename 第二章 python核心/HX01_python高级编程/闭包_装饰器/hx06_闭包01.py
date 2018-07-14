# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/5


# def test():
#     print('----1-----')
#
# test()

# In[9]: test
# Out[9]: <function __main__.test>
# In[10]:cd = test
# In[11]:cd()
# {'b': 200, 'a': 100}

# 闭包: 函数里面再定义函数,且里面的函数用到了 外面函数的变量. 整个这个大函数叫闭包

def test2(num1):

    print('===1===')

    def test_in():
        print('===2===')
        print(num1+100)

    print('===3===')
    return test_in  # 注意,这里返回的是函数的引用

a = test2(100)
print('*'*50)
a()
print('$'*50)
##############################################################
def test(num1):

    print('===1===')

    def test_in(num2):
        print('===2===')
        print(num1+num2)

    print('===3===')
    return test_in  # 注意,这里返回的是函数的引用

b = test(100)
print('*'*50)
b(10)