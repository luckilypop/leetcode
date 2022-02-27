#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/2/27 16:45
# @Author  : yq
# @File    : 面试0207链表相交.py
# @Software: PyCharm

'''
class Solution:
    def getIntersectionNode(self, headA, headB):
        curA = headA
        curB = headB
        lenA, lenB =0, 0
        # 求链表长度
        while curA != None:
            lenA += 1
            curA = curA.next
        while curB != None:
            lenB += 1
            curB = curB.next

        curA = headA
        curB = headB
        # 让curA为最长链表的头，lenA为其长度
        if lenB > lenA:
            tempLen = lenA
            lenA = lenB
            lenB = tempLen

            tempNode = curA
            curA = curB
            curB = tempNode
        # 求长度差
        gap = lenA - lenB
        # 让curA和curB在同一起点上（末尾位置对齐）
        while gap:
            curA = curA.next
            gap -= 1
        # 遍历curA 和 curB，遇到相同则直接返回
        while curA != None:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None


    # 方法2：???
    def getIntersectionNode_2(self, headA, headB):
        cur_a, cur_b = headA, headB  # 用两个指针代替a和b

        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB  # 如果a走完了，那么就切换到b走
            cur_b = cur_b.next if cur_b else headA  # 同理，b走完了就切换到a

        return cur_a
