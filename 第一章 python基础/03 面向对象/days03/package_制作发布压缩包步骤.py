# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/9

days03 20/37 左右讲解

1. 创建setup.py

from distutils.core import setup

setup(name="package", #包名
      version="1.0",    # 版本
      description="sdf",  #描述信息
      long_description="sdf", # 完整描述信息
      author="dfsa",      #作者
      url="主页",
      py_modules=["package.send_message",
                  "package.receiver_message"]
      )
有关字典参数的详细信息，参考官方网站
https://docs.python.org/2/distutils/apiref.html

2. 构建模块
$ python3 setup.py build

3. 生成发布压缩包
$ python3 setup.py sdist #在dist目录下生成打包的压缩包