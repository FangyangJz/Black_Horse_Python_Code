# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/3

students = [
    {'name':'Atu',
     'age':20,
     'gender':True,
     'height':1.7,
     'weight':75.0},
    {'name':'xiaomei',
     'age':19,
     'gender':False,
     'height':1.6,
     'weight':45.0}
]

find_name = 'Atu'  #vars

for stu_dict in students:

    print stu_dict

    if stu_dict['name'] == find_name:

        print "Find %s" % find_name

        break
        # 如果找到了，应该直接退出循环，而不再遍历后续的元素
else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
    # 还希望得到一个统一的提示
    print ('sorry, there is no %s' % find_name)

print "end"