#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/9 8:55
# @Author  : yq
# @File    : 101对称二叉树.py
# @Software: PyCharm

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self,left,right):
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left == None and right == None:
            return True
        elif left.val != right.val:
            return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        issame = outside and inside
        return issame
if __name__ == '__main__':

    # 建立dta
    nodelist = [TreeNode(i) for i in [1,2,2,3,4,4,3]]
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
    m = s.isSymmetric(Tree)

    print("二叉树是否对称%s" % (m))


