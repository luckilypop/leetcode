#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/3/11 10:03
# @Author  : yq
# @File    : 257二叉树的所有路径.py
# @Software: PyCharm

'''


class Solution:
    def binaryTreePaths(self, root) :
        path = ''
        result = []
        if not root: return result
        self.traversal(root, path, result)
        return result

    def traversal(self, cur, path, result):
        path += str(cur.val)
        # 若当前节点为leave，直接输出
        if not cur.left and not cur.right:
            result.append(path)

        if cur.left:
            # + '->' 是隐藏回溯
            self.traversal(cur.left, path + '->', result)

        if cur.right:
            self.traversal(cur.right, path + '->', result)
