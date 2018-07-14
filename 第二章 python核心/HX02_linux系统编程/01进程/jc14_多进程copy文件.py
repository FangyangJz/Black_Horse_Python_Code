# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/4/1


import os
from multiprocessing import Pool, Manager


def copy_file_task(name, oldFolderName, newFolderName, queue):
    '''完成拷贝一个文件的功能'''
    file_read = open(oldFolderName + '/' + name)
    file_write = open(newFolderName + '/' + name, 'w')

    content = file_read.read()
    file_write.write(content)

    file_read.close()
    file_write.close()

    queue.put(name)

def main():
    # 0. 获取要copy文件夹的名字
    oldFolderName = input('请输入要拷贝的文件夹名字:')
    newFolderName = oldFolderName + '-复件'

    # 1. 创建一个文件夹
    # print(newFolderName)
    os.mkdir(newFolderName)

    # 2. 获取old文件夹中的所有文件的名字
    file_names = os.listdir(oldFolderName)
    # print(file_names)

    # 3. 使用多进程方式copy原文件夹中的文件到新文件夹中
    po = Pool(5)
    queue = Manager().Queue()

    for name in file_names:
        po.apply_async(copy_file_task,args=(name, oldFolderName, newFolderName, queue))

    num = 0
    allNum = len(file_names)
    while True:
        queue.get()
        num += 1
        copyRate = num/allNum
        print('\rcopy的进度是:%.2f%%' %(copyRate*100),end='')
        if num==allNum:
            break

    po.close()
    po.join()
    print('')

# windows 下可能有编码问题, 导致copy的文件内容啥也没有, linux下正常(除了最后一个文件没拷贝全)
if __name__ == '__main__':
    main()
