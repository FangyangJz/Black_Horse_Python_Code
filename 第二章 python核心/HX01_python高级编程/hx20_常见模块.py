# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/30

# hashlib
import hashlib

m = hashlib.md5()
m.update('你的密码'.encode('utf-8')) # 更新哈希对象
print(m.hexdigest()) # 返回十六进制数字字符串