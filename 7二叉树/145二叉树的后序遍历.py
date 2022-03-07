#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/7 9:16
# @Author  : yq
# @File    : 145二叉树的后序遍历.py
# @Software: PyCharm

'''
# 定义二叉树
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right =right

class Solution:
    def postorderTraversal(self,root):
        result = []
        def travelsal(root):
            if root == None:
                return
            # 后序：左右中
            travelsal(root.left)
            travelsal(root.right)
            result.append(root.val)


        travelsal(root)
        return result

if __name__ == '__main__':
    # 建立dta
    nodelist = [TreeNode(i) for i in [1, 2, 3, 14, 5, 6, 10]]
    # 说明left和right的值：都是地址
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    nodelist[2].left = nodelist[5]
    nodelist[2].right = nodelist[6]
    # Tree是地址
    Tree = nodelist[0]

    s = Solution()
    m = s.postorderTraversal(Tree)

    print("二叉树的后序遍历为%s" % (m))
