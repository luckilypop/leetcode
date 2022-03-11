#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/8 9:41
# @Author  : yq
# @File    : 589N叉树的前序遍历.py
# @Software: PyCharm

'''
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        result = []
        def helper(root):
            if not root:
                return
            result.append(root.val)
            for child in root.children:
                helper(child) ## ?如何调用地址
        helper(root)
        return result

if __name__ == '__main__':
    # 建立dta
    nodelist = [Node(i) for i in [1,None,3,2,4,None,5,6]]
    # 说明left和right的值：都是地址
    nodelist[0].children = [3,2,4]
    nodelist[2].children = [5,6]

    Tree = nodelist[0]

    s = Solution()
    m = s.preorder(Tree)

    print("二叉树的前序遍历为%s" % (m))
