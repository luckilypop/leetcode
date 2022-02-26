#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/26 10:25
# @Author  : yq
# @File    : 206翻转链表.py
# @Software: PyCharm

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(ListNode):
    # 双指针法
    def reverseList(self, head):
        cur = head
        pre = None
        while cur!= None:
            temp = cur.next
            cur.next = pre

            pre = cur
            cur = temp
        return pre

    # 迭代法
    def reverseList_2(self, head):
        def reverse(pre, cur):
            if not cur:
                return pre
            temp = cur.next
            cur.next = pre

            return reverse(cur, temp)
        return reverse(None, head)

