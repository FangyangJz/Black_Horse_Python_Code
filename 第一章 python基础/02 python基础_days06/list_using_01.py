# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/22

name_list = ['zhangsan', 'lisi', 'wangwu']

print (name_list[2])
print (name_list.index('wangwu'))

# 2 修改
name_list[1] = '李四'

# 3.增加
name_list.append('大哥')
name_list.append('dage')
name_list.insert(1,'xiaomeimei')

# extend 可以把其他列表追加到当前列表后面
temp_list = ['wukong','bajie','shashidi']
name_list.extend(temp_list)

# 4.删除
name_list.remove('wukong')
# pop默认可以把列表中最后一个元素删除
name_list.pop()
name_list.pop(1)    #指定索引位置删除

# name_list.clear() #python3 中的命令，可以清空列表
del name_list[0]  #del本质上是用来将一个变量从内存中删除，后续的代码就不能使用这个变量了

print (name_list)
