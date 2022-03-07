#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/7 9:27
# @Author  : yq
# @File    : 94二叉树的中序遍历.py
# @Software: PyCharm

'''
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self,root):
        result = []
        def travalsal(root):
            if root==None:
                return
            travalsal(root.left)
            result.append(root.val)
            travalsal(root.right)
        travalsal(root)
        return result


if __name__ == '__main__':
    nodelist = [TreeNode(i) for i in [1,2,3,4,5,6]]

    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    nodelist[2].left = nodelist[5]

    tree = nodelist[0]

    s = Solution()
    m = s.inorderTraversal(tree)
    print("二叉树的中序遍历为%s" % (m))
