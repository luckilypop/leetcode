#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/11 9:53
# @Author  : yq
# @File    : 222完全二叉树的节点个数.py
# @Software: PyCharm

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root):
        return self.getNode(root)
    def getNode(self,root):
        if not root:
            return 0
        leftNum = self.getNode(root.left)
        rightNum = self.getNode(root.right)
        num = leftNum + rightNum + 1
        return num

