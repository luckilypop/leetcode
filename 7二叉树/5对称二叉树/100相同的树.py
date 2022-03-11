#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/9 9:08
# @Author  : yq
# @File    : 100相同的树.py
# @Software: PyCharm

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        return self.compare(p,q)
    def compare(self,p,q):
        if p == None and q!= None:
            return False
        elif p != None and q == None:
            return False
        elif p == None and q == None:
            return True
        elif p.val != q.val:
            return False

        out_left = self.compare(p.left,q.left)
        out_right = self.compare(p.right,q.right)
        return out_left and out_right

