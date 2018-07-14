# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/9

安装：
$ tar -zxvf package.tar.gz
$ sudo python3 setup.py install 会把package安装到 python3 lib 库里面去




删除：

查找文件存在路径，可以在python环境下
import package
package.__file__  #查看包的完整路径

切换到dist-package目录下
sudo rm package*

