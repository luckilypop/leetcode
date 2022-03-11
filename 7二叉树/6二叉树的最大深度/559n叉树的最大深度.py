#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/10 11:20
# @Author  : yq
# @File    : 559n叉树的最大深度.py
# @Software: PyCharm

'''
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        return 1 + max((self.maxDepth(ch) for ch in root.children), default = 0)