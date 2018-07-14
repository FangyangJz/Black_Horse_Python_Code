# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/1/3


class Node(object):

    def __init__(self, elem):
        self.elem = elem
        self.next = None

class Single_link_List(object):

    '''
    is_empty() 链表是否为空
    length() 链表长度
    travel() 遍历整个链表
    add(item) 链表头部添加元素
    append(item) 链表尾部添加元素
    insert(pos, item) 指定位置添加元素
    remove(item) 删除节点
    search(item) 查找节点是否存在
    '''
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        '链表是否为空'
        return self.__head == None

    def length(self):
        '链表长度'
        # cur游标,用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next


    def add(self, item):
        '''链表头部添加元素, 头插法'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''链表尾部添加元素, 尾插法'''
        node = Node(item)

        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head

            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素'''
        pre = self.__head
        count = 0
        while count <:
            pre = pre.next
            count += 1

    def remove(self, item):
        '''删除节点'''
        pass

    def search(self, item):
        '''查找节点是否存在'''
        pass

if __name__ == '__main__':

    ll = Single_link_List()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    print('-'*50)
    ll.append(1)
    ll.append(2)
    ll.add(8)
    ll.append(3)
    print(ll.travel())
