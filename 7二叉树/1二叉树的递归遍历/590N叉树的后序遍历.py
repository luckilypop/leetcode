#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/8 9:49
# @Author  : yq
# @File    : 590N叉树的后序遍历.py
# @Software: PyCharm

'''

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root):
        result = []

        def helper(root):
            if not root:
                return

            for child in root.children:
                helper(child)
            result.append(root.val)

        helper(root)
        return result



