#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/27 15:59
# @Author  : yq
# @File    : 19删除链表的倒数第N个节点.py
# @Software: PyCharm

'''
# 题目
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(next=head)
        fast, slow = dummy, dummy
        while n!=0: #fast先往前走n步
            fast = fast.next
            n -= 1
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        # fast 走到结尾后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next
        return dummy.next
