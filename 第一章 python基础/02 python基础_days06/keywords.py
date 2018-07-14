# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/10/22

import keyword
print keyword.kwlist
print len(keyword.kwlist)

python3_keywords_list = ['False','None','True','and','as'
                         ,'assert','break','class','continue'
                         ,'def','del','elif','else','except'
                         ,'finally','for','from','global','if'
                         ,'import','in','is','lambda','nonlocal'
                         ,'not','or','pass','raise','return','try'
                         ,'while','with','yield']

print len(python3_keywords_list)

python2_keywords_list = keyword.kwlist
print python3_keywords_list

#求 python2 和 python3 中的不同
ret = list(set(python3_keywords_list) ^ set(python2_keywords_list))
print ret

#求 python2 和 python3 中的相同
print list(set(python2_keywords_list).union(set(python3_keywords_list)))
print len(list(set(python2_keywords_list).union(set(python3_keywords_list))))