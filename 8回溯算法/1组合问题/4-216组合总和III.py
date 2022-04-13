#!/usr/bin/env python
# encoding: utf-8

'''
# @Time    : 2022/4/13 14:14
# @Author  : yq
# @File    : 4-216组合总和III.py
# @Software: PyCharm

'''
def combinationSum3(n, k):
    res = []
    path = []
    sum_now = 0
    def backtrack(n, k, startindex):
        nonlocal sum_now
        if sum_now > n:
            return
        if len(path) == k:
            if sum_now == n:
                res.append(path[:])
            return
        for i in range(startindex, n - (k-len(path)) + 2):
            path.append(i)
            sum_now += i
            backtrack(n, k, i+1)
            path.pop()
            sum_now -= i
    backtrack(n, k, 1)
    return res
print(combinationSum3(18,2))