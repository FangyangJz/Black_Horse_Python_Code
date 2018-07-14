# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/10

import os

文件操作：
    os.rename(源文件名，目标文件名)
    os.remove(文件名)

目录操作：
    os.listdir(目录名)     目录列表
    os.mkdir(目录名)       创建目录
    os.rmdir(目录名)       删除目录
    os.getcwd()           获取当前目录
    os.chdir(目标目录)      修改工作目录
    os.path.isdir(文件路径) 判断是否是文件
提示： 文件或者目录操作都支持 相对路径 和 绝对路径