#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/11 10:00
# @Author  : yq
# @File    : 110平衡二叉树.py
# @Software: PyCharm

'''
class Solution:
    def isBalanced(self, root):
        if self.get_hight(root) != -1:
            return True
        else:
            return False

    def get_hight(self,root):
        if not root:
            return 0
        left = self.get_hight(root.left)

        right = self.get_hight(root.right)
        if abs(left-right) > 1:
            return -1
        if left == -1 or right == -1:
            return -1
        else:
            return 1+max(left,right)