#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/10 9:43
# @Author  : yq
# @File    : 104二叉树最大深度.py
# @Software: PyCharm

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self,root):
        return self.getdepth(root)
    def getdepth(self,node):
        if not node:
            return 0
        leftdepth = self.getdepth(node.left)
        rightdepth = self.getdepth(node.right)
        depth = 1+ max(leftdepth,rightdepth)
        return depth
if __name__ == '__main__':
    # 建立dta
    nodelist = [TreeNode(i) for i in [1, 2, 3, 14, 5, 6, 10]]
    # 说明left和right的值：都是地址
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]

    nodelist[2].left = nodelist[3]
    nodelist[2].right = nodelist[4]
    nodelist[3].left = nodelist[5]
    nodelist[5].right = nodelist[6]
    # Tree是地址
    Tree = nodelist[0]

    s = Solution()
    m = s.maxDepth(Tree)

    print("二叉树的前序遍历为%s" % (m))

