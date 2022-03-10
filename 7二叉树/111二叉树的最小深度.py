#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/10 11:18
# @Author  : yq
# @File    : 111二叉树的最小深度.py
# @Software: PyCharm

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)  # 获得左子树的最小高度
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)  # 获得右子树的最小高度
        return min_depth + 1
