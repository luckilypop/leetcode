#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/25 10:25
# @Author  : yq
# @File    : 203移除链表元素.py
# @Software: PyCharm

'''
# 题目
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

# 定义一个单链表节点
class ListNode:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next

class Linklist:  # 封装链表相关
    def __init__(self):
        self.head = None

    # 将传入的数组转化为链表
    def initList(self, data):
        # data 不为空时候，创建头结点
        while data:
            # 创建头节点
            self.head = ListNode(data[0])
            r = self.head  # 头结点
            p = self.head  # 指针
            # p作为指针，逐个为 data 内的数据创建结点, 建立链表
            for i  in data[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
            return r

    # 打印单链表
    def printList(self, head):
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

class Solution:
    # 方法一：虚拟结点的方式
    def removeElements(self, head, val):
        dummy_head = ListNode(next = head)
        cur = dummy_head
        while cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next

    # 方法二：原来链表直接删除
    def removeElements_2(self, head, val):
        if head == None:
            return head
        # 删除头结点
        while head != None and head.val == val:
            head = head.next

        # 删除非头结点
        cur = head
        while cur != None and cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

if __name__ == '__main__':
    # 实例化单链表
    a = Linklist()
    data = [2,3,6,1,2]
    # 数组转换为单链表ll
   #  ll = a.initList(data)
    # 初始化类
    b = Solution()
    # 调用函数，ll为单链表，结果temp也为单链表
    temp = b.removeElements_2(a.initList(data),6)
    # 打印temp单链表的值
    print(a.printList(temp))


