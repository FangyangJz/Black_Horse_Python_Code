# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/25

poem = ['\t\n登鹳雀楼',
        '王之涣',
        '白日依山尽\t\n',
        '黄哥入海流\t']


for poem_str in poem:

    # 先使用strip方法去除字符串中的空白字符
    # 再用center方法剧中显示文本
    print ("|%s|" %(poem_str.center(20)))
    print ("|%s|" %(poem_str.strip().center(20)))