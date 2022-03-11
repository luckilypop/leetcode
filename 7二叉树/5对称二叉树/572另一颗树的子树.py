#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/9 9:09
# @Author  : yq
# @File    : 572另一颗树的子树.py
# @Software: PyCharm

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:

        return self.preorder(root, subRoot)

    def preorder(self, root, subRoot):
        if not root:
            return False
        resleft = self.preorder(root.left, subRoot)
        resright = self.preorder(root.right, subRoot)
        # 如果 根节点就不同 就直接返回左右子树的结果 跳过这一个root所在的子树
        if root.val != subRoot.val:
            return resleft or resright
        # 如果 根节点相同 就可以开始一次判断
        return resleft or resright or self.helper(root, subRoot)

    def helper(self, root, subRoot):
        # 保证 子树的构造相同
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        # 保证 子树的值 都是相同的
        return root.val == subRoot.val and self.helper(root.left, subRoot.left) and self.helper(root.right,
                                                                                                subRoot.right)

if __name__ == '__main__':

    # 建立dta
    nodelist = [TreeNode(i) for i in [3,4,5,1,2,None,None,None,None,0]]
    # 说明left和right的值：都是地址
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    nodelist[4].left = nodelist[9]

    # Tree是地址
    Tree = nodelist[0]
    subnode = [TreeNode(i) for i in [4,1,2]]
    subnode[0].left = subnode[1]
    subnode[0].right = subnode[2]

    subTree = subnode[0]

    s = Solution()
    m = s.isSubtree(Tree,subTree)

    print("二叉树是否对称%s" % (m))
