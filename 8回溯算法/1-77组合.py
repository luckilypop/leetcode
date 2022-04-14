


#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/13 9:54
# @Author  : yq
# @File    : 1-77组合.py
# @Software: PyCharm

'''
def combine(n, k):
    res = []
    path = []
    def backtrack(n, k, startindex):
        if len(path) == 2:
            res.append(path[:])
            return
        for i in range(startindex, n+1):
            path.append(i)
            backtrack(n, k, i+1)
            path.pop()
    backtrack(n, k, 1)
    return res
