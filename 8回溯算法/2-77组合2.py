#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/13 10:40
# @Author  : yq
# @File    : 2-77组合2.py
# @Software: PyCharm

'''


def combiine(n, k):
    res = []
    path = []
    def backtrack(n, k ,startindex):
        if len(path) == 2:
            res.append(path[:])
            return
        for i in range(startindex, n-(k-len(path))+2):
            path.append(i)
            backtrack(n,k,i+1)
            path.pop()
    backtrack(n,k,1)
    return res