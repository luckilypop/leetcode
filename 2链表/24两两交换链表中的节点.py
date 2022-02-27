#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/27 15:32
# @Author  : yq
# @File    : 24两两交换链表中的节点.py
# @Software: PyCharm

'''
# 题目
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
# 你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self,head):
        res = ListNode(next=head)
        pre = res
        # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = cur # pre = pre.next.next

        return res.next
