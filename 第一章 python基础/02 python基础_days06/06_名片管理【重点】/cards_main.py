#! D:\Anaconda2\python.exe
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/11/5

import cards_tools

while True:
    # while True + break
    #TODO 显示功能菜单 （主动提示）
    cards_tools.show_menu()

    action_str = raw_input('请选择希望执行的操作：')
    print '您选择的操作是:【%s】 , 类型是: %s'%(action_str,type(action_str))

    # 1，2，3针对名片的操作
    if action_str in ['1','2','3']:

        #新增名片
        if action_str == '1':
            cards_tools.new_card()
        #显示全部
        elif action_str == '2':
            cards_tools.show_all()
        #查询名片
        elif action_str == '3':
            cards_tools.search_card()


    # 0 退出系统
    elif action_str == '0':
        print 'welcome see you again!'
        break

        # pass #如果在程序开发时，不希望立刻编写分支内部代码，用pass


    # 其他内容，输入错误，需要提示用户重新输入
    else:
        print '您输入的不正确，请重新选择'