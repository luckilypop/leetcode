#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/7 9:53
# @Author  : yq
# @File    : 102二叉树的层序遍历.py
# @Software: PyCharm

'''
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self,root):
        res = []
        def helper(root,depth):
            if root == None:
                return []
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            if root.left:
                helper(root.left,depth+1)
            if root.right:
                helper(root.right,depth+1)
        helper(root,0)
        return res



if __name__ == '__main__':
    nodelist = [TreeNode(i) for i in [1, 2, 3, 4, 5, 6]]

    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    nodelist[2].left = nodelist[5]

    tree = nodelist[0]

    s = Solution()
    m = s.levelOrder(tree)
    print("二叉树的层序遍历为%s" % (m))
